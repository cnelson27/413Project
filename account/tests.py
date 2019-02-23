from django.test import TestCase
from account import models as amod

# Create your tests here.
class AccountTests(TestCase):
    fixtures = [ 'account.yaml' ]

    def test_user_get(self):
        u2 = amod.User.objects.get(id=2)
        self.assertEqual(u2.first_name, 'Homer', 'Name should have been Homer')

    def test_user_create(self):
        u = amod.User()
        u.first_name = 'Harry'
        u.last_name = 'Potter'
        u.username = 'harry'
        u.set_password = 'hermione'
        u.save()
        u2 = amod.User.objects.get(u.username)
        self.assertEqual(u.first_name, u2.first_name, msg='User is not created successfully')