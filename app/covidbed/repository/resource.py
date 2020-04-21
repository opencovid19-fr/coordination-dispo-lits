from datetime import datetime
from covidbed.model import Organization, Platform, Contact, Availability


def create_availability(platform, organization, date, functional_unit=None, bed=None, supply=None, human=None, contact=None):
    assert isinstance(platform, Platform)
    assert isinstance(organization, Organization)
    assert isinstance(date, datetime)
    assert bed is None or isinstance(bed, dict)
    assert supply is None or isinstance(supply, dict)
    assert human is None or isinstance(human, dict)
    assert contact is None or isinstance(contact, dict) or isinstance(contact, Contact)

    if isinstance(contact, dict):
        contact_obj = Contact(**contact)
        contact_obj.save()
    else:
        contact_obj = contact

    obj = Availability(date=date, platform=platform, organization=organization,
                       functional_unit=functional_unit,
                       contact=contact_obj, bed=bed, supply=supply, human=human)
    obj.save()
    return obj


def get_contact(id):
    return Contact.query.filter(Contact.id==id).first()
