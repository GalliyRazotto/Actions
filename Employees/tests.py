from django.test import TestCase
from .models import Person
# Create your tests here.


class TestModel(TestCase):
    def setUp(self):
        self.person = Person.objects.create(firstName='Kirill',
                                            lastName='Popov')

    def tearDown(self):
        self.person.delete()
