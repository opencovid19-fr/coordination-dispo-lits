from covidbed.model import User, Organization, Platform, FinessEtablissement, Address, Company, OrganizationType, Region


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


def create_organization(name, reg_code=None, address=None, company=None, etfiness=None):
    assert address is None or isinstance(address, dict)
    assert company is None or isinstance(company, dict)
    assert etfiness is None or isinstance(etfiness, dict)
    assert etfiness or company

    address_obj = Address(**address) if address else None
    company_obj = Company(**company) if company else None
    etfiness_obj = FinessEtablissement(**etfiness) if etfiness else None
    if etfiness:
        obj = Organization(name=name, reg_code=reg_code, type=OrganizationType.finess_et,
                           address=address_obj, data=etfiness_obj)
    else:
        obj = Organization(name=name, reg_code=reg_code, type=OrganizationType.finess_et,
                           address=address_obj, data=company_obj)
    obj.save()
    return obj


def get_organization(id):
    return Organization.query.filter(Organization.id == id).first()


def get_or_create_region(**kwargs):
    reg = Region.query.filter(Region.code==kwargs["code"]).first()
    if not reg:
        reg = Region(**kwargs)
        reg.save()
    return reg




