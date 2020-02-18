from django.test import TestCase


class LandingPageTest(TestCase):

    def test_00_landing_page_exists(self):
        response = self.client.get(path='')
        header = bytes("Zacznij pomagać", encoding='utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='index.html')
        self.assertIn(header, response.content)
