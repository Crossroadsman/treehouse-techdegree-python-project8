from django.test import Client, TestCase
from django.urls import reverse


class ViewTest(TestCase):

    def test_redirects_to_catalog(self):
        self.client = Client()
        redirect_target = '/catalog/'

        response = self.client.get(reverse('index'))

        self.assertRedirects(response, redirect_target)
