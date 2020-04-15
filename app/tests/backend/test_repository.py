from repository.user import create_user

from tests.utils.mixins import BaseTest


class TestUser(BaseTest):
    fixtures = ["users.json"]

    def test_create_user_organization(self):
        params = {
            "email": 'bill@example.fr',
            "password": 'super-secret-password',
            "firstname": "Bill",
            "lastname": "Jackson",
            "phone_number": "0234434343"
        }
        organization = {
            "name": "Ma plateform",
            "address":  {
                    "street": "30 rue des visiteurs",
                    "zipcode": "54344",
                    "city": "covid-19",
                    "lon": None,
                    "lat": None
            },
            "company": {
                "siret": "1234543789789"
            }
        }
        obj = create_user(params, organization)
        self.assertEqual(obj.id, 1)

    def test_create_user_platform(self):
        params = {
            "email": 'bill@example.fr',
            "password": 'super-secret-password',
            "firstname": "Bill",
            "lastname": "Jackson",
            "phone_number": "0234434343"
        }
        organization = {
            "name": "Ma plateform",
        }
        obj = create_user(params, platform=organization)
        self.assertEqual(obj.id, 1)
        expected_result = {'id': 1, 'email': 'bill@example.fr',
                           'firstname': 'Bill', 'lastname': 'Jackson',
                           'phone_number': '0234434343'}
        for k, v in expected_result.items():
            self.assertEqual(v, getattr(obj, k))

        expected_org = {'id': 1, 'name': 'Ma plateform'}
        for k, v in expected_org.items():
            self.assertEqual(v, getattr(obj.organisation, k))


