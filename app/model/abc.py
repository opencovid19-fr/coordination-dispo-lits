"""Define an Abstract Base Class (ABC) for models."""
import datetime
import enum
from weakref import WeakValueDictionary
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import inspect
from sqlalchemy.orm import aliased
import sqlalchemy.types as types


db = SQLAlchemy()
ma = Marshmallow()


class MetaBaseModel(db.Model.__class__):
    """ Define a metaclass for the BaseModel to implement `__getitem__` for managing aliases """

    def __init__(cls, *args):
        super().__init__(*args)
        cls.aliases = WeakValueDictionary()

    def __getitem__(cls, key):
        try:
            alias = cls.aliases[key]
        except KeyError:
            alias = aliased(cls)
            cls.aliases[key] = alias
        return alias


class BaseModel:
    """ Generalize __init__, __repr__ and to_json
        Based on the models columns """

    print_filter = ()
    to_json_filter = ()

    def __init__(self,  **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        """ Define a base way to print models
            Columns inside `print_filter` are excluded """
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
            if column not in self.print_filter
        })

    @property
    def json(self):
        """ Define a base way to jsonify models
            Columns inside `to_json_filter` are excluded """

        def get_value(value):
            if isinstance(value, BaseModel):
                return value.json
            if isinstance(value, datetime.date):
                return value.isoformat()
            if isinstance(value, enum.Enum):
                return value.value
            return value

        return {
            column: get_value(value)
            for column, value in self._to_dict().items()
            if column not in self.to_json_filter
        }

    def _to_dict(self):
        """ This would more or less be the same as a `to_json`
            But putting it in a "private" function
            Allows to_json to be overriden without impacting __repr__
            Or the other way around
            And to add filter lists """
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self.__class__).attrs
        }

    # Method to save user to DB
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Method to remove user from DB
    def remove(self):
        db.session.delete(self)
        db.session.commit()

    def refresh(self):
        db.session.refresh(self)


class ChoiceType(types.TypeDecorator):

    impl = types.String

    def __init__(self, choices, **kw):
        self.choices = dict(choices)
        super(ChoiceType, self).__init__(**kw)

    def process_bind_param(self, value, dialect):
        return [k for k, v in self.choices.iteritems() if v == value][0]

    def process_result_value(self, value, dialect):
        return self.choices[value]


class Base(db.Model, BaseModel):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)

