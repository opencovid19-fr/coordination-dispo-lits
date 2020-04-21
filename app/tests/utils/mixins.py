import unittest
import json

from flask_fixtures import FixturesMixin


from server import server
from covidbed.model.abc import db

server.config['TESTING'] = True


class BaseTest(unittest.TestCase, FixturesMixin):
    app = server
    db = db

    def setUp(self):
        self.client = server.test_client()

    def tearDown(self):
        # remove client session if not cannot drop test database
        db.session.remove()


class BaseAuthMixin(object):

    def authenticate(self, email, password):
        response = self.client.post(
            '/api/auth/login',
            json={'email': email, 'password': password},
            content_type="application/json"

        )

        if response.status_code != 200:
            raise Exception("Invalide user")
        result = json.loads(response.data.decode('utf-8'))
        return result["token"]

    def get(self, url, token, params=None):

        return self.client.get(
            url,
            data=params,
            headers={'Authorization': 'Bearer ' + token}
        )

    def post(self, url, token, params=None):

        return self.client.post(
            url,
            json=params,
            headers={'Authorization': 'Bearer ' + token},
            content_type='application/json'
        )

    def put(self, url, token, params=None):
        return self.client.put(
            url,
            json=params,
            headers={'Authorization': 'Bearer ' + token},
            content_type='application/json'
        )

    def delete(self, url, token):
        return self.client.delete(
            url,
            headers={'Authorization': 'Bearer ' + token}
        )


