from django.test import TestCase
from account import models as amod

# Create your tests here.
class AccountTests(TestCase):
    fixtures = [ 'account.yaml' ]

    def test_user_get(self):
        u2 = amod.User.objects.get(id=2)
        # BAD BAD WOLF - just while developing this test
        print('>>>>', u2.first_name)

