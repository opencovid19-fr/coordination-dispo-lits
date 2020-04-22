from flask import request
from flask_jwt_extended import current_user, jwt_required
from flask_restful import Resource
from flask_restful_swagger import swagger

from covidbed.validator import resource as ress_validator
from covidbed.repository import user as user_repository, resource as ress_repo
from covidbed.serializer.resource import ResourceSerializer,ResourceCreationResponseSerializer


class ResourcesApi(Resource):
    method_decorators = [jwt_required]

    @swagger.operation(
        notes='Resources',
        responseClass=ResourceCreationResponseSerializer.__name__,
        nickname='resources',
        parameters=[
            {
                "name": "body",
                "description": "resource availability by date and finess etablissement. ",
                "required": True,
                "allowMultiple": False,
                "dataType": ResourceSerializer.__name__,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 201,
                "message": "Resource is created."
            },
            {
                "code": 400,
                "message": "Parametor's errors"
            }

        ])
    def post(self):
        user = current_user
        params = request.json
        validator = ress_validator.AvailabilityRequest()
        errors = validator.validate(params, many=False)
        if errors:
            return {"errors": [{"code": f"BAD_PARAM_{k.upper()}", "message": "\n".join(v)} for k, v in
                               errors.items()]}, 400

        params = validator.load(params)
        errors = []
        etablissement = user_repository.get_organization(params.get("etablissement_id"))
        if not etablissement:
            errors.append({"code": f"UNKNOWN_ETABLISSEMENT", "message": "Unknown etablissement"})

        contact = params.get("contact")
        cont = None
        if contact:
            if contact.get("id"):
                cont = ress_repo.get_contact(contact.get("id"))
                if not cont:
                    errors.append({"code": f"UNKNOWN_CONTACT", "message": "Unknown contact"})
            else:
                cont = {f: contact.get(f) for f in ["lastname", "firstname", "email", "phone_number", "comment"]
                        if contact.get(f) is not None}
                if len(cont) < 4:
                    errors.append({"code": f"CREATE_CONTACT",
                                   "message": "lastname, firstname, email, phone_number are required"})

        platform = user.organization

        if errors:
            return {"errors": errors}, 400

        obj = ress_repo.create_availability(platform, etablissement,
                                            date=params.get('date'),
                                            functional_unit=params.get("functional_unit"),
                                            contact=cont,
                                            bed=params.get("bed"),
                                            supply=params.get("supply"),
                                            human=params.get("human"))

        return {'id': str(obj.id)}, 201
