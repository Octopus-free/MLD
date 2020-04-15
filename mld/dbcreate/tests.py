from django.test import TestCase
from .models import AlgorithmsBook, MetricsBook
from ManagingUsers.models import MLDUser
from mixer.backend.django import mixer
from django.test import Client


class AlgorithmsBookTestCase(TestCase):

    def test_str_method(self):

        user = MLDUser.objects.create_user(username='test_user', password='Test123', email='Test12@test.com')
        str_method = AlgorithmsBook.objects.create(algo_name='test_algo', algo_desc='test_desc', user=user)
        self.assertEqual(str(str_method), 'test_algo')


class MetricsBookTestCase(TestCase):

    def test_str_method(self):

        str_method = mixer.blend(MetricsBook, metric_name='test_metric')
        self.assertEqual(str(str_method), 'test_metric')


class OpenViewsTestCase(TestCase):

    def setUp(self):

        self.client = Client()
        self.user = MLDUser.objects.create_superuser(username='Testuser', password='test123', email='test112@test.com')

    def test_views_status(self):

        response_main = self.client.get('/')
        self.assertEqual(response_main.status_code, 200)

        response_db = self.client.get('/db/')
        self.assertEqual(response_db.status_code, 200)

    def test_login(self):

        response_add_info = self.client.get('/add/')
        self.assertEqual(response_add_info.status_code, 403)

        self.client.login(username=self.user.username, password='test123')

        response_login = self.client.get('/add/')
        self.assertEqual(response_login.status_code, 200)


class PaginatorTestCase(TestCase):

    def setUp(self):

        self.client = Client()
        self.user = MLDUser.objects.create_superuser(username='Testuser', password='test123', email='test112@test.com')

    def test_page_three(self):
        response_page_three = self.client.get('/db/?page=3/')
        self.assertEqual(response_page_three.status_code, 404)

    def test_page_two(self):

        algo_1 = mixer.blend(AlgorithmsBook)
        algo_2 = mixer.blend(AlgorithmsBook)

        response_page_two = self.client.get('/db/?page=2')
        self.assertEqual(response_page_two.status_code, 200)
