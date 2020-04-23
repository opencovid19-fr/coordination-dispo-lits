from covidbed.model import Organization, OrganizationType, FinessEtablissement, Company


def create_organization(name, reg_code=None, address=None, company=None, etfiness=None):
    assert address is None or isinstance(address, dict)
    assert company is None or isinstance(company, dict)
    assert etfiness is None or isinstance(etfiness, dict)
    assert etfiness or company

    address_obj = Address(**address) if address else None
    company_obj = Company(**company) if company else None
    etfiness_obj = FinessEtablissement(**etfiness) if etfiness else None
    if etfiness:
        obj = Organization(
            name=name, reg_code=reg_code, type=OrganizationType.finess_et, address=address_obj, data=etfiness_obj
        )
    else:
        obj = Organization(
            name=name, reg_code=reg_code, type=OrganizationType.company, address=address_obj, data=company_obj
        )
    obj.save()
    return obj


def get_organization_by_id(id):
    return Organization.query.filter(Organization.id == id).first()


def get_organization_by_siret(siret):
    return (
        Organization.query.filter(Organization.type == OrganizationType.company)
        .join(Company, Company.id == Organization.object_id)
        .filter(Company.siret == siret)
        .first()
    )


def get_organization_by_finess_et(finess_et):
    return (
        Organization.query.filter(Organization.type == OrganizationType.finess_et)
        .join(FinessEtablissement, FinessEtablissement.id == Organization.object_id)
        .filter(FinessEtablissement.finess_et == finess_et)
        .first()
    )


def get_organization_by_finess_ej(finess_ej):
    return (
        Organization.query.filter(Organization.type == OrganizationType.finess_et)
        .join(FinessEtablissement, FinessEtablissement.id == Organization.object_id)
        .filter(FinessEtablissement.finess_ej == finess_ej)
        .first()
    )
