import json
import unittest

from model.user import User

from test.utils.mixins import BaseTest, BaseAuthMixin


class TestAuth(BaseTest):
    fixtures = ["users.json"]

    def test_routes(self):
        response = self.client.get(
            '/'
        )
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        params = {
            "email": 'joe@example.fr',
            "password": 'super-secret-password'
        }
        response = self.client.post(
            '/api/auth/login',
            json=params,
            content_type="application/json"

        )
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertIn("token", result)

    def test_signup(self):
        params = {
            "email": 'bill@example.fr',
            "password": 'super-secret-password'
        }
        response = self.client.post(
            '/api/auth/signup',
            json=params,
            content_type="application/json"

        )
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertIn("id", result)
        self.assertEqual(result["id"], '2')


class TestUser(BaseAuthMixin, BaseTest):
    fixtures = ["users.json"]


    def test_get_user(self):
        token = self.authenticate('joe@example.fr', 'super-secret-password')
        url = 'api/users/1'
        response = self.get(url, token)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        for k, v in {'email': 'joe@example.fr',
                     'firstname': None,
                     'id': 1,
                     'lastname': None
                     }.items():
            self.assertIn(k, result)
            self.assertEqual(result[k], v)

    def test_update_user(self):
        token = self.authenticate('joe@example.fr', 'super-secret-password')
        url = 'api/users/1'
        response = self.put(url, token, {'firstname': "titi", "lastname": 'toto'})
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))

        for k, v in {'email': 'joe@example.fr',
                     'firstname': 'titi',
                     'id': 1,
                     'lastname': 'toto'
                     }.items():
            self.assertIn(k, result)
            self.assertEqual(result[k], v)

    def test_delete_user(self):
        token = self.authenticate('joe@example.fr', 'super-secret-password')
        url = 'api/users/1'
        response = self.delete(url, token)
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(User.query.filter_by(email='bill@example.fr').first())


if __name__ == '__main__':
    unittest.main()
