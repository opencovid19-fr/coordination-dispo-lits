
import datetime

from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import  Resource
from flask_restful_swagger import swagger

from covidbed.serializer.orga import OrganizationSerializer

from covidbed.repository import orga as orga_repository
from covidbed.validator import orga as orga_validator

from sqlalchemy.orm.exc import NoResultFound

class OrganizationAPI(Resource):
    method_decorators = [jwt_required]

    # @swagger.operation(
    #     notes='Organizations',
    #     responseClasse=OrganizationSerializer.__name__,
    #     nickname='organizations',
    #     parameters=[
    #         {
    #             "name": "body",
    #             "description": "organisations which might provide resources. It could be a company or a finess instutition."
    #             "required": True,
    #             "allowMultiple": False,
    #             "dataType": OrganizationSerializer.__name__,
    #             "paramType": "body",
    #         }
    #     ]
    # )

    def get(self):
        params = request.json
        validator = orga_validator.OrganizationRequest()
        errors = validator.validate(params, many=False)
        if errors:
            return {"errors": [{"code": f"BAD_PARAM_{k.upper()}", "message": "\n".join(v)} for k, v in
                               errors.items()]}, 400
        params = validator.load(params)
        errors = []
        
        # First we evaluate if the organization already exists
        orga = None
        if "id" in params:
            orga = orga_repository.get_organization_by_id(params["id"])
        elif "company" in params:
            orga = orga_repository.get_organization_by_siret(params["company"]["siret"])
        elif "finess_etablissement" in params:
            if ("finess_et" in params["finess_etablissement"]) and ("finess_ej" not in params["finess_etablissement"]):
                orga = orga_repository.get_organization_by_finess_et(params["finess_etablissement"]["finess_et"])
            elif ("finess_ej" in params["finess_etablissement"]) and ("finess_et" not in params["finess_etablissement"]):
                orga = orga_repository.get_organization_by_finess_ej(params["finess_etablissement"]["finess_ej"])
            else:
                # If both et and ej provided, we check they corrresponds to the same entitty
                orga_et = orga_repository.get_organization_by_finess_et(params["finess_etablissement"]["finess_et"])
                orga_ej = orga_repository.get_organization_by_finess_ej(params["finess_etablissement"]["finess_ej"])
                if orga_et == orga_ej:
                    orga = orga_et
                else:
                    errors.append({
                        "code": f"MISMATCHING_ET_EJ",
                        "message": "finess_et and finess_ej don't correspond to the same entity"
                    })

        if errors:
            return {"errors": errors}, 400
        
        if orga is None:
            errors.append({
                "code": f"NOT_FOUND",
                "message": "The entity you are looking for doesn't exist yet"
            })
            return {"errors": errors}, 400

        if orga is not None:
            return orga.json, 200
