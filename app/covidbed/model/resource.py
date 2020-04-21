from .abc import db, Base
from .orga import Organization, Platform


class Contact(Base):
    __tablename__ = 'ress_contact'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    comment = db.Column(db.Text, nullable=True)


class Availability(Base):
    __tablename__ = 'ress_availability'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    functional_unit = db.Column(db.String(25), nullable=True)
    bed = db.Column(db.JSON, nullable=True)
    supply = db.Column(db.JSON, nullable=True)
    human = db.Column(db.JSON, nullable=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('ress_contact.id'))
    contact = db.relationship(Contact)

    platform_id = db.Column(db.Integer, db.ForeignKey('orga_platform.id'), nullable=False)
    platform = db.relationship(Platform)

    organization_id = db.Column(db.Integer, db.ForeignKey('orga_organization.id'), nullable=False)
    organization = db.relationship(Organization, backref="availabilities")


