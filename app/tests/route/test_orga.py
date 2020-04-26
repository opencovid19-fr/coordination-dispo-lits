import json
import unittest

from covidbed.model import User

from tests.utils.mixins import BaseTest, BaseAuthMixin


class TestOrga(BaseAuthMixin, BaseTest):
    fixtures = ["users.json", "resources.json"]

    def test_get_orga_id(self):

        token = self.authenticate("joe@example.fr", "super-secret-password")
        url = "api/organizations"
        params = {"id": 1001}
        expected_result = {
            "orga": {
                "address": {
                    "created_at": "2020-04-15T12:40:14.462544",
                    "updated_at": "2020-04-15T12:40:14.462544",
                    "street": "900 RTE DE PARIS",
                    "insee_code": "11451",
                    "zipcode": "11440",
                    "city": "VIRIAT",
                    "lon": 5.20859613227913,
                    "lat": 46.2227447821928,
                },
                "data": {
                    "created_at": "2020-04-15T12:40:14.462544",
                    "updated_at": "2020-04-15T12:40:14.462544",
                    "id": 1001,
                    "finess_et": "123",
                    "finess_ej": "124",
                },
                "created_at": "2020-04-15T12:40:14.462544",
                "updated_at": "2020-04-15T12:40:14.462544",
                "id": 1001,
                "name": "CH FAKE 1",
                "type": 1,
                "reg_code": None,
                "address_id": 1001,
            },
            "retrived_key": "id",
        }
        response = self.get(url, token, params=params)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode("utf-8"))
        self.assertEqual(result, expected_result)

    def test_get_orga_siret(self):
        token = self.authenticate("joe@example.fr", "super-secret-password")
        url = "api/organizations"
        params = {"siret": "12"}
        expected_result = {
            "orga": {
                "address": {
                    "created_at": "2020-04-15T12:40:14.462544",
                    "updated_at": "2020-04-15T12:40:14.462544",
                    "street": "7 Rue du 14 Juillet",
                    "insee_code": "45258",
                    "zipcode": "45390",
                    "city": "PUISEAUX",
                    "lon": 2.469977,
                    "lat": 48.2041928,
                },
                "data": {
                    "created_at": "2020-04-15T12:40:14.462544",
                    "updated_at": "2020-04-15T12:40:14.462544",
                    "id": 2001,
                    "siret": "12",
                },
                "created_at": "2020-04-15T12:40:14.462544",
                "updated_at": "2020-04-15T12:40:14.462544",
                "id": 1003,
                "name": "COMPANY FAKE 1",
                "type": 2,
                "reg_code": None,
                "address_id": 2001,
            },
            "retrived_key": "siret",
        }
        response = self.get(url, token, params=params)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode("utf-8"))
        self.assertEqual(result, expected_result)

    def test_get_orga_finess_et(self):
        token = self.authenticate("joe@example.fr", "super-secret-password")
        url = "api/organizations"
        params = {"finess_et": "123"}
        expected_result = {
            "orga": {
                "address": {
                    "created_at": "2020-04-15T12:40:14.462544",
                    "updated_at": "2020-04-15T12:40:14.462544",
                    "street": "900 RTE DE PARIS",
                    "insee_code": "11451",
                    "zipcode": "11440",
                    "city": "VIRIAT",
                    "lon": 5.20859613227913,
                    "lat": 46.2227447821928,
                },
                "data": {
                    "created_at": "2020-04-15T12:40:14.462544",
                    "updated_at": "2020-04-15T12:40:14.462544",
                    "id": 1001,
                    "finess_et": "123",
                    "finess_ej": "124",
                },
                "created_at": "2020-04-15T12:40:14.462544",
                "updated_at": "2020-04-15T12:40:14.462544",
                "id": 1001,
                "name": "CH FAKE 1",
                "type": 1,
                "reg_code": None,
                "address_id": 1001,
            },
            "retrived_key": "finess_et",
        }
        response = self.get(url, token, params=params)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode("utf-8"))
        self.assertEqual(result, expected_result)

    def test_get_orga_finess_ej(self):
        token = self.authenticate("joe@example.fr", "super-secret-password")
        url = "api/organizations"
        params = {"finess_ej": "124"}
        expected_result = {
            "orga": {
                "address": {
                    "created_at": "2020-04-15T12:40:14.462544",
                    "updated_at": "2020-04-15T12:40:14.462544",
                    "street": "900 RTE DE PARIS",
                    "insee_code": "11451",
                    "zipcode": "11440",
                    "city": "VIRIAT",
                    "lon": 5.20859613227913,
                    "lat": 46.2227447821928,
                },
                "data": {
                    "created_at": "2020-04-15T12:40:14.462544",
                    "updated_at": "2020-04-15T12:40:14.462544",
                    "id": 1001,
                    "finess_et": "123",
                    "finess_ej": "124",
                },
                "created_at": "2020-04-15T12:40:14.462544",
                "updated_at": "2020-04-15T12:40:14.462544",
                "id": 1001,
                "name": "CH FAKE 1",
                "type": 1,
                "reg_code": None,
                "address_id": 1001,
            },
            "retrived_key": "finess_ej",
        }
        response = self.get(url, token, params=params)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode("utf-8"))
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
