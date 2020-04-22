from flask import request
from flask_jwt_extended import current_user, jwt_required
from flask_restful import Resource
from flask_restful_swagger import swagger

from covidbed.validator import resource as ress_validator
from covidbed.repository import resource as ress_repository, orga as orga_repository
from covidbed.serializer.resource import (ResourceSerializer, ResourceCreationResponseSerializer,
                                          ResourceListResponseSerializer)
from covidbed.util.validator import parse_params


class ResourcesApi(Resource):
    method_decorators = [jwt_required]

    @swagger.operation(
        notes="Resources",
        responseClass=ResourceListResponseSerializer.__name__,
        nickname='products',
        parameters=[
            {
                "name": "page",
                "description": "page number",
                "required": True,
                "allowMultiple": False,
                "dataType": "int",
                "paramType": "body"
            },
            {
                "name": "size",
                "description": "number of items returned",
                "required": False,
                "default": 10,
                "allowMultiple": False,
                "dataType": "int",
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "List of products."
            }

        ])
    @parse_params(
        {'name': 'page', 'type': int, "default": 1},
        {'name': 'size', 'type': int, "default": 10},
    )
    def get(self, params):
        user = current_user

        obj = ress_repository.list_availabilities_by_platform(user.organization, params.get("page"), params.get("size"))
        return {"total": obj.total,
                "page": params.get("page"),
                "size": params.get("size"),
                "results": [item.json for item in obj.items]}, 200

    @swagger.operation(
        notes='Resources',
        responseClass=ResourceCreationResponseSerializer.__name__,
        nickname="resources",
        parameters=[
            {
                "name": "body",
                "description": "resource availability by date and finess etablissement. ",
                "required": True,
                "allowMultiple": False,
                "dataType": ResourceSerializer.__name__,
                "paramType": "body",
            }
        ],
        responseMessages=[
            {"code": 201, "message": "Resource is created."},
            {"code": 400, "message": "Parametor's errors"},
        ],
    )
    def post(self):
        user = current_user
        params = request.json
        validator = ress_validator.AvailabilityRequest()
        errors = validator.validate(params, many=False)
        if errors:
            return (
                {"errors": [{"code": f"BAD_PARAM_{k.upper()}", "message": "\n".join(v)} for k, v in errors.items()]},
                400,
            )

        params = validator.load(params)
        errors = []
        etablissement = orga_repository.get_organization_by_id(params.get("etablissement_id"))
        if not etablissement:
            errors.append({"code": f"UNKNOWN_ETABLISSEMENT", "message": "Unknown etablissement"})

        contact = params.get("contact")
        cont = None
        if contact:
            if contact.get("id"):
                cont = ress_repository.get_contact(contact.get("id"))
                if not cont:
                    errors.append({"code": f"UNKNOWN_CONTACT", "message": "Unknown contact"})
            else:
                cont = {
                    f: contact.get(f)
                    for f in ["lastname", "firstname", "email", "phone_number", "comment"]
                    if contact.get(f) is not None
                }
                if len(cont) < 4:
                    errors.append(
                        {"code": f"CREATE_CONTACT", "message": "lastname, firstname, email, phone_number are required"}
                    )

        platform = user.organization

        if errors:
            return {"errors": errors}, 400

        obj = ress_repository.create_availability(
            platform,
            etablissement,
            date=params.get("date"),
            functional_unit=params.get("functional_unit"),
            contact=cont,
            bed=params.get("bed"),
            supply=params.get("supply"),
            human=params.get("human"),
        )

        return {"id": str(obj.id)}, 201
