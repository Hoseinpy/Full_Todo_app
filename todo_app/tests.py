from django.test import TestCase
from django.urls import reverse


class MainTest(TestCase):
    
    def test_main_page(self):
        client = self.client
        res = client.get(reverse('index'))
        self.assertEqual(res.status_code, 200)