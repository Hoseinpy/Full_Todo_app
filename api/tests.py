from django.urls import reverse
from rest_framework.test import APITestCase


class TodoTestCase(APITestCase):

    def test_todo_list(self):
        res = self.client.get(reverse('todo_list_api'))
        self.assertEqual(res.status_code, 200)

    def test_add_todo(self):
        res = self.client.post(reverse('add_todo_api'), data={'title':'two'})
        self.assertEqual(res.status_code, 201)