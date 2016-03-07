# -*- coding: utf-8 -*-

import simplejson as json
from django.test import TestCase
from todomvc.models import Task


class GETIndexTest(TestCase):

    def setUp(self):
        self.tasks = [
            Task.objects.create(
                title='Buy groceries'
            ),
            Task.objects.create(
                title='Do laundry'
            )
        ]

    def test_it_responds_an_array_of_tasks(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
        tasks_list = json.loads(response.content)

        for expected, actual in zip(tasks_list, self.tasks):
            self.assertEqual(expected['id'], actual.id)
