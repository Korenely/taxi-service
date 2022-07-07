from django.test import TestCase
from taxi.models import *


class ModelsTests(TestCase):
    def test_Manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(name="manufacturer", country="Poland")
        self.assertEqual(str(manufacturer), f"{manufacturer.name} {manufacturer.country}")

    def test_Driver_str(self):
        driver = Driver.objects.create(license_number=1, username="Test", first_name="Test", last_name="Test")
        self.assertEqual(str(driver), f"{driver.username} ({driver.first_name} {driver.last_name})")

    def test_Car_str(self):
        manufacturer = Manufacturer.objects.create(name="manufacturer", country="Poland")
        car = Car.objects.create(model="Test", manufacturer=manufacturer)

        self.assertEqual(str(car), car.model)

