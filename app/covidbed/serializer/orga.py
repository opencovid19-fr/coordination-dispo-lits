from flask_restful_swagger import swagger
from flask_restful import fields


@swagger.model
class CompanySerializer:
    resource_fields = {
        "id": fields.Integer(attribute="company_id"),
        "siret": fields.String,
    }


@swagger.model
class FinessEtablissementSerializer:
    resource_fields = {
        "id": fields.Integer(attribute="finess_etablissement_id"),
        "finess_et": fields.String,
        "finess_ej": fields.String,
    }


@swagger.model
class AddressSerializer:
    resource_fields = {
        "id": fields.Integer,
        "street": fields.String,
        "insee_code": fields.String,
        "zipcode": fields.String,
        "city": fields.String,
        "lon": fields.Float,
        "lat": fields.Float,
        # "organizations": fields.List(fields.Nested(OrganizationSerializer.resource_fields)),
    }


@swagger.model
class OrganizationSerializer:
    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "company": fields.Nested(CompanySerializer.resource_fields),
        "finess_etablissement": fields.Nested(FinessEtablissementSerializer.resource_fields),
        "address": fields.Nested(AddressSerializer),
    }
