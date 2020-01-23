import unittest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APILiveServerTestCase
from nine.versions import DJANGO_GTE_2_1
import factories
from foo.models import Bar

__title__ = 'nonefield.tests.test_drf_integration'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2020 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
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
        self.foo = factories.FooFactory()
        self.foo_url = reverse(
            'fooapi-detail',
            args=[self.foo.pk],
        )
        self.client.logout()

    @classmethod
    def setUpTestData(cls):
        """Load initial data for the TestCase"""
        cls.bar_id = 1
        cls.bar = Bar.objects.get(pk=cls.bar_id)
        cls.bar_url = reverse(
            'barapi-detail',
            args=[cls.bar_id],
        )

    def tearDown(self):
        """Set up."""
        super(NoneFieldDRFIntegrationTestCase, self).tearDown()
        self.client.logout()

    def test_01_options_action_public_form(self):
        """Test OPTIONS action call for public form."""
        # Testing OPTIONS action call
        options_response = self.client.options(self.foo_url)
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
            self.foo_url,
            {
                "id": self.foo.pk,
                "title": "Everything store final.",
                "text": "Wide explain force ability manage car return. Camera "
                        "pass itself eat along reason media. Single garden "
                        "expect deal picture degree nor security.",
                "context_text": "Haha",
                "url": "http://testserver/fooapi/{}/".format(self.foo.pk),
            },
            format='json'
        )
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.foo.refresh_from_db()
        self.assertDictEqual(
            dict(put_response.data),
            {
                "id": self.foo.pk,
                "title": "Everything store final.",
                "text": "Wide explain force ability manage car return. Camera "
                        "pass itself eat along reason media. Single garden "
                        "expect deal picture degree nor security.",
                "context_text": "Haha" if DJANGO_GTE_2_1 else "",
                "url": "http://testserver/fooapi/{}/".format(self.foo.pk),
            }
        )

    def test_03_bar_options_action_public_form(self):
        """Test OPTIONS action call for public form."""
        # Testing OPTIONS action call
        options_response = self.client.options(self.bar_url)
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

    def test_04_bar_put_action_public_form(self):
        """Test PUT action call for public form."""
        # Testing PUT action call
        put_response = self.client.put(
            self.bar_url,
            {
                "id": self.bar_id,
                "title": "Everything store final.",
                "text": "Wide explain force ability manage car return. Camera "
                        "pass itself eat along reason media. Single garden "
                        "expect deal picture degree nor security.",
                "context_text": "Haha",
                "url": "http://testserver/barapi/{}/".format(self.bar_id),
            },
            format='json'
        )
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.bar.refresh_from_db()
        self.assertDictEqual(
            dict(put_response.data),
            {
                "id": self.bar_id,
                "title": "Everything store final.",
                "text": "Wide explain force ability manage car return. Camera "
                        "pass itself eat along reason media. Single garden "
                        "expect deal picture degree nor security.",
                "context_text": "Haha" if DJANGO_GTE_2_1 else "",
                "url": "http://testserver/barapi/{}/".format(self.bar_id),
            }
        )


if __name__ == '__main__':
    unittest.main()
