from django.test import SimpleTestCase


# Create your tests here.
class NewsTests(SimpleTestCase):
    def test_code_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

