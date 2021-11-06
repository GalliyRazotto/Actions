from django.test import TestCase
from .models import Person, test_functions
# Create your tests here.


class TestPerson(TestCase):
    def setUp(self):
        self.person = Person.objects.create(firstName='Kirill',
                                            lastName='Popov')

    def test_test_function(self):
        res = test_functions()
        self.assertTrue(res)

    def tearDown(self):
        self.person.delete()
