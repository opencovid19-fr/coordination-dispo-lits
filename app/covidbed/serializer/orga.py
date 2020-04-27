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
    }


@swagger.model
@swagger.nested(company=CompanySerializer.__name__)
@swagger.nested(finess_etablissement=FinessEtablissementSerializer.__name__)
@swagger.nested(address=AddressSerializer.__name__)
class OrganizationSerializer:
    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "reg_code": fields.String,
        "type": fields.Integer,
        "address_id": fields.Integer,
        "address": fields.Nested(AddressSerializer),
    }


@swagger.model
class OrganizationSearchRequestSerializer:
    resource_fields = {
        "id": fields.Integer,
        "siret": fields.String,
        "finess_et": fields.String,
        "finess_ej": fields.String,
    }


@swagger.model
@swagger.nested(organization=OrganizationSerializer.__name__)
class OrganizationSearchResponseSerializer:
    resource_fields = {
        "organization": fields.Nested(OrganizationSerializer.resource_fields),
        "retrieved_key": fields.String(),
    }
