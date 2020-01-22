from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APILiveServerTestCase

__title__ = 'nonefield.tests.test_drf_integration'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'NoneFieldDRFIntegrationTestCase',
)


class NoneFieldDRFIntegrationTestCase(APILiveServerTestCase):
    """DRF integration tests."""

    @classmethod
    def setUpClass(cls):
        super(NoneFieldDRFIntegrationTestCase, cls).setUpClass()
        cls.setUpTestData()

    def setUp(self):
        """Set up."""
        super(NoneFieldDRFIntegrationTestCase, self).setUp()
        self.client.logout()

    def tearDown(self):
        """Set up."""
        super(NoneFieldDRFIntegrationTestCase, self).tearDown()
        self.client.logout()

    @classmethod
    def setUpTestData(cls):
        """Load initial data for the TestCase"""
        cls.id = 1
        cls.url = reverse(
            'fooapi-detail',
            args=[cls.id],
        )

    def test_01_options_action_public_form(self):
        """Test OPTIONS action call for public form."""
        # Testing OPTIONS action call
        options_response = self.client.options(self.url)
        self.assertEqual(options_response.status_code, status.HTTP_200_OK)
        self.assertIn('actions', options_response.data)
        self.assertIn('PUT', options_response.data['actions'])
        self.assertDictEqual(
            options_response.data['actions']['PUT'],
            {
                "id": {
                    "type": "integer",
                    "required": False,
                    "read_only": True,
                    "label": "Id"
                },
                "title": {
                    "type": "string",
                    "required": True,
                    "read_only": False,
                    "label": "Title",
                    "max_length": 256
                },
                "text": {
                    "type": "string",
                    "required": True,
                    "read_only": False,
                    "label": "Text"
                },
                "context_text": {
                    "type": "field",
                    "required": False,
                    "read_only": True
                },
                "url": {
                    "type": "field",
                    "required": False,
                    "read_only": True,
                    "label": "Url"
                }
            }
        )

    def test_02_put_action_public_form(self):
        """Test PUT action call for public form."""
        # Testing PUT action call
        put_response = self.client.put(
            self.url,
            {
                "id": 1,
                "title": "Everything store final.",
                "text": "Wide explain force ability manage car return. Camera "
                        "pass itself eat along reason media. Single garden "
                        "expect deal picture degree nor security.",
                "context_text": "Haha",
                "url": "http://testserver/fooapi/1/",
            },
            format='json'
        )
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        import pytest; pytest.set_trace()
        self.assertDictEqual(
            dict(put_response.data),
            {
                "id": 1,
                "title": "Everything store final.",
                "text": "Wide explain force ability manage car return. Camera "
                        "pass itself eat along reason media. Single garden "
                        "expect deal picture degree nor security.",
                "context_text": "",
                "url": "http://testserver/fooapi/1/",
            }
        )
