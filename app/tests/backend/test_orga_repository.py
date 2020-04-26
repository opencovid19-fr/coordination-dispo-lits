from covidbed.model import OrganizationType
from covidbed.repository import orga as orga_repository

from tests.utils.mixins import BaseTest


class TestOrga(BaseTest):
    fixtures = ["resources.json"]

    def test_create_organization_siret(self):
        siret_number = "12"
        organization = {
            "name": "Ma plateform",
            "address": {
                "street": "30 rue des visiteurs",
                "zipcode": "54344",
                "city": "covid-19",
                "lon": None,
                "lat": None,
            },
            "company": {"siret": siret_number},
        }
        organization = orga_repository.create_organization(**organization)
        print(organization)
        print(organization.data)
        print(organization.object_type)
        self.assertEqual(organization.id, 1)
        self.assertEqual(organization.type, OrganizationType.company)
        self.assertEqual(organization.data.siret, siret_number)

    def test_create_organization_finess(self):
        finess_et = "12"
        finess_ej = "13"
        organization = {
            "name": "Ma plateform",
            "address": {
                "street": "30 rue des visiteurs",
                "zipcode": "54344",
                "city": "covid-19",
                "lon": None,
                "lat": None,
            },
            "etfiness": {"finess_et": finess_et, "finess_ej": finess_ej},
        }
        organization = orga_repository.create_organization(**organization)
        self.assertEqual(organization.id, 1)
        self.assertEqual(organization.type, OrganizationType.finess_et)
        self.assertEqual(organization.data.finess_et, finess_et)
        self.assertEqual(organization.data.finess_ej, finess_ej)

    def test_get_by_finess_id(self):
        obj = orga_repository.get_organization_by_id(1002)
        self.assertEqual(obj.id, 1002)

    def test_get_by_siret(self):
        obj = orga_repository.get_organization_by_siret("12")
        self.assertEqual(obj.id, 1003)

    def test_get_by_finess_et(self):
        obj = orga_repository.get_organization_by_finess_et("123")
        self.assertEqual(obj.id, 1001)

    def test_get_by_finess_ej(self):
        obj = orga_repository.get_organization_by_finess_ej("124")
        self.assertEqual(obj.id, 1001)
