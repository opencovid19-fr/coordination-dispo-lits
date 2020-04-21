import datetime
from flask_bcrypt import generate_password_hash, check_password_hash
from sqlalchemy_utils import generic_relationship
from werkzeug.security import generate_password_hash, check_password_hash

from .abc import db, Base


class User(Base):
    __tablename__ = 'auth_user'

    print_filter = ('password','object_type', 'object_id')
    to_json_filter = ('password', 'object_type', 'object_id')

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    password = db.Column(db.String(120))
    phone_number = db.Column(db.String(10), nullable=True)

    # This is used to discriminate between the linked tables.
    object_type = db.Column(db.Unicode(255))
    # This is used to point to the primary key of the linked row.
    object_id = db.Column(db.Integer)
    organisation = generic_relationship(object_type, object_id)

    def __init__(self, email=None, password=None, **kwargs):
        super(User, self).__init__(email=email, password=password, **kwargs)
        if email:
            self.email = email.lower()
        if password:
            self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

