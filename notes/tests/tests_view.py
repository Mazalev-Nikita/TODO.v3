"""
 Получить список записей без фильтров
 получить все записи со статусом "Активно" (пункт 9  Фильтровать по одному или нескольким состояниям)
 получить все записи со статусом "Активно" и "Выполнено" (пункт 9  Фильтровать по одному или нескольким состояниям)
 получить все важные записи (пункт 10 Фильтр по важности)
 Получить все публичные записи (пункт 11 Фильтр по публичности)
 Получить важные непубличные записи со статусом "Активно"(пункт 12 Все фильтры могут быть применены
"""

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()

from notes.models import Note


class TestNoteListCreate(APITestCase):
    USER_1 = dict(
        username="ivan",
        password="password1",
    )
    USER_2 = dict(
        username="anna",
        password="password2",
    )

    @classmethod
    def setUpTestData(cls):
        users = [
            User(**cls.USER_1),
            User(**cls.USER_2),
        ]
        User.objects.bulk_create(users)
        cls.db_user_1 = users[0]

        notes = [
            Note(title="title_1",
                 message='message1',
                 public='True',
                 importance='False',
                 create_date="2022-23-06T00:00:00Z",
                 complete='False',
                 complete_date="2022-25-12T00:00:00Z",
                 author=users[0],
                 status='Активно'),
            Note(title="title_2",
                 message='message2',
                 public='False',
                 importance='True',
                 create_date="2022-23-06T00:00:00Z",
                 complete='True',
                 complete_date="2022-24-12T00:00:00Z",
                 author=users[1],
                 status='Активно'),
        ]
        Note.objects.bulk_create(notes)

    def test_no_filters(self):
        url = ''
        resp = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        resp_data = resp.data
        self.assertEqual(2, len(resp_data))

    def test_active(self):
        url = ''
        filters = {'status': 'Активно'}
        resp = self.client.get(url, filters)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        resp_data = resp.data
        self.assertEqual(2, len(resp_data))

    def test_active_and_complete(self):
        url = ''
        filters = {'status': 'Активно', 'complete': 'True'}
        resp = self.client.get(url, filters)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        resp_data = resp.data
        self.assertEqual(1, len(resp_data))

    def test_important(self):
        url = ''
        filters = {'importance': 'True'}
        resp = self.client.get(url, filters)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        resp_data = resp.data
        self.assertEqual(1, len(resp_data))

    def test_public(self):
        url = ''
        filters = {'public': 'True'}
        resp = self.client.get(url, filters)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        resp_data = resp.data
        self.assertEqual(1, len(resp_data))

    def nonpublic_and_active(self):
        url = ''
        filters = {'public': 'False', 'status': 'Активно'}
        resp = self.client.get(url, filters)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        resp_data = resp.data
        self.assertEqual(1, len(resp_data))