from marshmallow import Schema, fields, validate, ValidationError, validates_schema


class OrganizationSearchRequest(Schema):
    id = fields.Integer()
    siret = fields.String()
    finess_et = fields.String()
    finess_ej = fields.String()

    @validates_schema
    def combinations(self, data, **kwargs):
        if not set(["id", "siret", "finess_et", "finess_ej"]).intersection(data):
            raise ValidationError("Not enough informations")
        # Checks if siret or (finess_et or finess_ej) in the fields
        if ("siret" in data) and (("finess_et" in data) or ("finess_ej" in data)):
            raise ValidationError("Siret and finess are incompatible")
