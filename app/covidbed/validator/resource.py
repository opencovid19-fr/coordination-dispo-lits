from marshmallow import Schema, fields, validate


class Human(Schema):
    reanimators_count = fields.Integer(required=False)
    need_staff = fields.Integer(required=False, validate=validate.OneOf([1, 0]))


class Supply(Schema):
    respirators_count = fields.Integer(required=False)
    efp2_mask_count = fields.Integer(required=False)
    chir_mask_count = fields.Integer(required=False)
    blouses_count = fields.Integer(required=False)
    gowns_count = fields.Integer(required=False)


class Bed(Schema):
    covid_available = fields.Integer(required=False)
    covid_used = fields.Integer(required=False)
    other_available = fields.Integer(required=False)
    other_used = fields.Integer(required=False)
    conventional_count = fields.Integer(required=False)
    continue_care_count = fields.Integer(required=False)
    reanimation_count = fields.Integer(required=False)
    post_urgency_count = fields.Integer(required=False)
    other_count = fields.Integer(required=False)


class Contact(Schema):
    id = fields.Integer(required=False)
    firstname = fields.String(required=False)
    lastname = fields.String(required=False)
    email = fields.Email(required=False)
    phone_number = fields.String(required=False)
    comment = fields.String(required=False)


class AvailabilityRequest(Schema):
    date = fields.DateTime(required=True)
    etablissement_id = fields.Integer(required=True)
    functional_unit = fields.String(required=False, allow_none=True)

    bed = fields.Nested(Bed, required=False, allow_none=True)
    supply = fields.Nested(Supply, required=False, allow_none=True)
    human = fields.Nested(Human, required=False, allow_none=True)

    contact = fields.Nested(Contact, required=False, allow_none=True)
