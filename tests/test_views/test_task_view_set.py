# -*- coding: utf-8 -*-

import json
from django.test import TestCase
from model_mommy import mommy
from todomvc.models import Task


class TaskViewSetTest(TestCase):

    def test_GET_tasks(self):
        tasks = mommy.make(
            Task,
            _quantity=2
        )
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
        tasks_list = json.loads(response.content)

        for expected, actual in zip(tasks_list, tasks):
            self.assertEqual(expected['id'], actual.id)

    def test_POST_tasks(self):
        title = 'Workout'
        response = self.client.post(
            '/tasks/',
            {
                'title': title
            })
        self.assertEqual(response.status_code, 201)
        task_set = Task.objects.filter(title=title)
        self.assertEqual(task_set.count(), 1)

    def test_GET_task(self):
        task = mommy.make(Task)
        response = self.client.get('/tasks/{0}/'.format(task.id))
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.content)
        self.assertEqual(task.title, response_json['title'])

    def test_PATCH_task(self):
        task = mommy.make(Task, completed=False)
        self.assertFalse(task.completed)
        response = self.client.patch(
            '/tasks/{0}/'.format(task.id),
            data=json.dumps({
                'completed': 1
            }),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        updated_task = Task.objects.get(id=task.id)
        self.assertTrue(updated_task.completed)

    def test_PUT_task(self):
        task = mommy.make(Task, completed=False)
        self.assertFalse(task.completed)
        response = self.client.put(
            '/tasks/{0}/'.format(task.id),
            data=json.dumps({
                'title': task.title,
                'completed': 1
            }),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        updated_task = Task.objects.get(id=task.id)
        self.assertTrue(updated_task.completed)

    def test_DELETE_task(self):
        task = mommy.make(Task)
        response = self.client.delete('/tasks/{0}/'.format(task.id))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Task.objects.filter(id=task.id).count(), 0)
