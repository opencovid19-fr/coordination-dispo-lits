from covidbed.model import User, Organization, Platform, FinessEtablissement, Address, Company, OrganizationType, Region
from covidbed.repository.orga import create_organization


def find_users():
    return [user.json for user in User.query]


def get_user_by_id(_id):
    """

    :param _id:
    :return:
    """
    return User.query.filter_by(id=_id).first()


def create_user(params, organization=None, platform=None):
    """

    :param params:
    :return:
    """
    assert isinstance(params, dict)
    assert organization is None or isinstance(organization, dict)
    assert platform is None or isinstance(platform, dict)

    if organization:
        org = create_organization(**organization)
    elif platform:
        org = Platform(**platform)
        org.save()
    else:
        org = None
    user = User(organization=org, **params)
    user.save()
    return user


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def get_or_create_region(**kwargs):
    reg = Region.query.filter(Region.code == kwargs["code"]).first()
    if not reg:
        reg = Region(**kwargs)
        reg.save()
    return reg
