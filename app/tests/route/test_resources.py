import unittest

from covidbed.model import Availability

from tests.utils.mixins import BaseTest, BaseAuthMixin


class TestResources(BaseTest, BaseAuthMixin):
    fixtures = ["users.json", "resources.json"]

    def test_create_availability(self):
        params = {
            "date": "2020-04-23T20:00:00",
            "etablissement_id": 1000,
            "functional_unit": None,
            "contact": {
                "lastname": "Mistigri",
                "firstname": "Le Chat",
                "email": "mistigry.lechat@email.fr",
                "phone_number": "0123456789",
                "comment": "ne pas deranger ....."
            },
            "bed": {
                "covid_available": 100,
                "covid_used": 50,
                "other_available": 150,
                "other_used": 25,
                "conventional_count": 45,
                "continue_care_count": 45,
                "reanimation_count": 45,
                "post_urgency_count": 54,
                "other_count": 50
            },
            "supply": {
                "respirators_count": 123,
                "efp2_masks_count": 343,
                "chir_masks_count": 345,
                "blouses_count": 23,
                "gowns_count": 12
            },
            "human": None
        }

        token = self.authenticate('joe@example.fr', 'super-secret-password')
        url = 'api/resources'
        response = self.post(url, token, params=params)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get("id"), '1')
        obj = Availability.query.get(1)
        self.assertEqual(obj.json["date"], "2020-04-23T20:00:00")
        self.assertEqual(obj.json["platform"],
                         {'created_at': '2020-04-15T12:40:14.462544', 'updated_at': '2020-04-15T12:40:14.462544',
                          'id': 1000, 'name': 'Covidmoiunlit'})
        self.assertEqual(obj.json["organization"],
                         {'address': {'created_at': '2020-04-15T12:40:14.462544',
                                      'updated_at': '2020-04-15T12:40:14.462544', 'street': '30 rue des visiteurs',
                                      'insee_code': None, 'zipcode': '54344', 'city': 'covid-19', 'lon': None,
                                      'lat': None}, 'data': {'created_at': '2020-04-15T12:40:14.462544',
                                                             'updated_at': '2020-04-15T12:40:14.462544', 'id': 1000,
                                                             'finess_et': '12345567890', 'finess_ej': '12345567890'},
                          'created_at': '2020-04-15T12:40:14.462544', 'updated_at': '2020-04-15T12:40:14.462544',
                          'id': 1000, 'name': 'Hopital du Paradis', 'type': 1, 'reg_code': None, 'address_id': 1000})
        self.assertEqual(obj.json["bed"],
                         {'continue_care_count': 45, 'covid_used': 50, 'reanimation_count': 45, 'other_used': 25,
                          'conventional_count': 45, 'other_count': 50, 'other_available': 150, 'covid_available': 100,
                          'post_urgency_count': 54})
        self.assertEqual(obj.json["supply"],
                         {'blouses_count': 23, 'gowns_count': 12,
                          'chir_masks_count': 345, 'efp2_masks_count': 343, 'respirators_count': 123})
        self.assertIsNone(obj.json["human"])
        for k, v in {'id': 1, "lastname": "Mistigri",
                     "firstname": "Le Chat",
                     "email": "mistigry.lechat@email.fr",
                     "phone_number": "0123456789",
                     "comment": "ne pas deranger ....."}.items():
            self.assertEqual(obj.json["contact"][k], v)

    def test_create_availability_with_existing_contact(self):
        params = {
            "date": "2020-04-23T20:00:00",
            "etablissement_id": 1000,
            "functional_unit": None,
            "contact": {
                "id": 1000,
            },
            "bed": {
                "covid_available": 100,
                "covid_used": 50,
                "other_available": 150,
                "other_used": 25,
                "conventional_count": 45,
                "continue_care_count": 45,
                "reanimation_count": 45,
                "post_urgency_count": 54,
                "other_count": 50
            },
            "supply": {
                "respirators_count": 123,
                "efp2_masks_count": 343,
                "chir_masks_count": 345,
                "blouses_count": 23,
                "gowns_count": 12
            },
            "human": None
        }

        token = self.authenticate('joe@example.fr', 'super-secret-password')
        url = 'api/resources'
        response = self.post(url, token, params=params)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get("id"), '1')
        obj = Availability.query.get(1)
        self.assertEqual(obj.json["date"], "2020-04-23T20:00:00")
        self.assertEqual(obj.json["platform"],
                         {'created_at': '2020-04-15T12:40:14.462544', 'updated_at': '2020-04-15T12:40:14.462544',
                          'id': 1000, 'name': 'Covidmoiunlit'})
        self.assertEqual(obj.json["organization"],
                         {'address': {'created_at': '2020-04-15T12:40:14.462544',
                                      'updated_at': '2020-04-15T12:40:14.462544', 'street': '30 rue des visiteurs',
                                      'insee_code': None, 'zipcode': '54344', 'city': 'covid-19', 'lon': None,
                                      'lat': None}, 'data': {'created_at': '2020-04-15T12:40:14.462544',
                                                             'updated_at': '2020-04-15T12:40:14.462544', 'id': 1000,
                                                             'finess_et': '12345567890', 'finess_ej': '12345567890'},
                          'created_at': '2020-04-15T12:40:14.462544', 'updated_at': '2020-04-15T12:40:14.462544',
                          'id': 1000, 'name': 'Hopital du Paradis', 'type': 1, 'reg_code': None, 'address_id': 1000})
        self.assertEqual(obj.json["bed"],
                         {'continue_care_count': 45, 'covid_used': 50, 'reanimation_count': 45, 'other_used': 25,
                          'conventional_count': 45, 'other_count': 50, 'other_available': 150, 'covid_available': 100,
                          'post_urgency_count': 54})
        self.assertEqual(obj.json["supply"],
                         {'blouses_count': 23, 'gowns_count': 12,
                          'chir_masks_count': 345, 'efp2_masks_count': 343, 'respirators_count': 123})
        self.assertIsNone(obj.json["human"])
        self.assertEqual(obj.json["contact"],
                         {'created_at': '2020-04-15T12:40:14.462544',
                          'updated_at': '2020-04-15T12:40:14.462544', 'id': 1000,
                          'firstname': 'joe', 'lastname': 'Leduc', 'email': 'joe@example.fr',
                          'phone_number': '0123456799', 'comment': None})

    def test_create_availability_unknown_contact(self):
        params = {
            "date": "2020-04-23T20:00:00",
            "etablissement_id": 1000,
            "functional_unit": None,
            "contact": {
                "id": 1,
            },
            "bed": {
                "covid_available": 100,
                "covid_used": 50,
                "other_available": 150,
                "other_used": 25,
                "conventional_count": 45,
                "continue_care_count": 45,
                "reanimation_count": 45,
                "post_urgency_count": 54,
                "other_count": 50
            },
            "supply": {
                "respirators_count": 123,
                "efp2_masks_count": 343,
                "chir_masks_count": 345,
                "blouses_count": 23,
                "gowns_count": 12
            },
            "human": None
        }

        token = self.authenticate('joe@example.fr', 'super-secret-password')
        url = 'api/resources'
        response = self.post(url, token, params=params)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'errors': [{'code': 'UNKNOWN_CONTACT',
                                                     'message': 'Unknown contact'}]})

    def test_create_availability_missing_contact_and_unknown_etablissement(self):
        params = {
            "date": "2020-04-23T20:00:00",
            "etablissement_id": 1,
            "functional_unit": None,
            "contact": {
                "firstname": "aadddd",
            },
            "bed": {
                "covid_available": 100,
                "covid_used": 50,
                "other_available": 150,
                "other_used": 25,
                "conventional_count": 45,
                "continue_care_count": 45,
                "reanimation_count": 45,
                "post_urgency_count": 54,
                "other_count": 50
            },
            "supply": {
                "respirators_count": 123,
                "efp2_masks_count": 343,
                "chir_masks_count": 345,
                "blouses_count": 23,
                "gowns_count": 12
            },
            "human": None
        }

        token = self.authenticate('joe@example.fr', 'super-secret-password')
        url = 'api/resources'
        response = self.post(url, token, params=params)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json,
                         {'errors': [{'code': 'UNKNOWN_ETABLISSEMENT', 'message': 'Unknown etablissement'},
                                     {'code': 'CREATE_CONTACT',
                                      'message': 'lastname, firstname, email, phone_number are required'}]})


if __name__ == '__main__':
    unittest.main()
