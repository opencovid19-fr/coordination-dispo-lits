from marshmallow import Schema, fields, validate, ValidationError, validates_schema


class Company(Schema):
    siret = fields.String(required=True)


class FinessEtablissement(Schema):
    finess_et = fields.String()
    finess_ej = fields.String()

    @validates_schema
    def finess_et_or_ej(self, data, **kwargs):
        if ("finess_et" not in data) and ("finess_ej" not in data):
            raise ValidationError("A finess_ej or a finess_et should be provided")


class OrganizationRequest(Schema):
    id = fields.Integer()
    company = fields.Nested(Company, required=False, allow_none=True)
    finess_etablissement = fields.Nested(FinessEtablissement, required=False, allow_none=True)
