from django.test import TestCase, Client
from django.urls import reverse


MANUFACTURER_LIST_URL = reverse("taxi:manufacturer-list")
CAR_LIST_URL = reverse("taxi:car-list")
DRIVER_LIST_URL = reverse("taxi:driver-list")


class PublicManufacturerListTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(MANUFACTURER_LIST_URL)

        self.assertNotEqual(res.status_code, 200)


class PublicCarListTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(CAR_LIST_URL)

        self.assertNotEqual(res.status_code, 200)


class DriverCarListTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(DRIVER_LIST_URL)

        self.assertNotEqual(res.status_code, 200)
