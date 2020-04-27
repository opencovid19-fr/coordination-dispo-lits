from flask_restful_swagger import swagger
from flask_restful import fields


@swagger.model
class HumanSerializer:
    resource_fields = {
        'reanimators_count': fields.Integer,
        'need_staff': fields.Integer,
    }


@swagger.model
class BedSerializer:
    resource_fields = {
        'covid_available': fields.Integer,
        'covid_used': fields.Integer,
        'other_available': fields.Integer,
        'other_used': fields.Integer,
        'conventional_count': fields.Integer,
        'continue_care_count': fields.Integer,
        'reanimation_count': fields.Integer,
        'post_urgency_count': fields.Integer,
        'other_count': fields.Integer,
    }


@swagger.model
class SupplySerializer:
    resource_fields = {
        'reanimators_count': fields.Integer,
        'efp2_masks_count': fields.Integer,
        'chir_masks_count': fields.Integer,
        'blouses_count': fields.Integer,
        'gowns_count': fields.Integer,
    }


@swagger.model
class ContactSerializer:
    resource_fields = {
        'id': fields.Integer,
        'firstname': fields.String,
        'lastname': fields.String,
        'phone_number': fields.String,
        'email': fields.String,
        'comment': fields.String,
    }


@swagger.model
@swagger.nested(bed=BedSerializer.__name__,
                supply=SupplySerializer.__name__,
                human=HumanSerializer.__name__,
                contact=ContactSerializer.__name__)
class ResourceSerializer:
    resource_fields = {
        'date': fields.DateTime,
        'etablissement_id': fields.Integer,
        'functional_unit': fields.String,
        'bed': fields.List(fields.Nested(BedSerializer.resource_fields)),
        'supply': fields.List(fields.Nested(SupplySerializer.resource_fields)),
        'human': fields.List(fields.Nested(HumanSerializer.resource_fields)),
        'contact': fields.List(fields.Nested(ContactSerializer.resource_fields))
    }
    required = ["date", 'etablissement_id']


@swagger.model
@swagger.nested(results=ResourceSerializer.__name__)
class ResourceListResponseSerializer:
    resource_fields = {
        'total': fields.Integer,
        'page': fields.Integer,
        'size': fields.Integer,
        'results': fields.List(fields.Nested(ResourceSerializer.resource_fields)),
    }
    required = ['total', "page", 'size', 'results']


@swagger.model
class ResourceCreationResponseSerializer:
    resource_fields = {
        'id': fields.Integer
    }
    required = ['id']
