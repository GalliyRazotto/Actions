from django.test import TestCase
from .models import Person
# Create your tests here.


class TestPerson(TestCase):
    def setUp(self):
        self.person = Person.objects.create(firstName='Kirill',
                                            lastName='Popov')

    def test_test_function(self):
        res = self.person
        self.assertTrue(isinstance(res, Person))

    def tearDown(self):
        self.person.delete()
