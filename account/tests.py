from django.test import TestCase
from account import models as amod
from datetime import datetime
from lxml import etree

# Create your tests here.
class AccountTests(TestCase):
    fixtures = [ 'account.yaml' ]

    def setUp(self):
        self.homer = amod.User.objects.get(username='homer')
        self.homer.set_password('doh!')
        self.homer.save()

    def test_user_get(self):
        u2 = amod.User.objects.get(id=2)
        u2.set_password('doh!')
        self.assertEqual(u2.first_name, 'Homer', 'Name should have been Homer')

    def test_user_login(self):
        credentials = {
            'username': 'homer',
            'password': 'doh!'
        }
        response = self.client.post('/account/login/', credentials)
        # get the request object (testing framework embeds it as response.wsgi_request)
        request = response.wsgi_request
        # this next line is ONLY for debugging the test - it should be removed after things work
        # self.print_html(response.content)
        # if it worked, then request.user will be the homer object and is_authenticated will be true
        self.assertTrue(request.user.is_authenticated, msg="User should have authenticated")
        self.assertEqual(request.user.id, self.homer.id, msg="User should have been homer")
        # if it worked, the response should be a redirect code (login.py returned HttpResponseRedirect)
        self.assertEqual(response.status_code, 302, msg="User wasn't redirected")

    def test_create_user(self):
        u = amod.User()
        u.id = 412
        u.first_name = 'Harry'
        u.last_name = 'Potter'
        u.email = 'hp@hogwarts.edu'
        u.set_password('hermione')
        u.save()
        u2 = amod.User.objects.get(412)
        self.assertEqual(u.first_name, u2.first_name, msg="User not saved correctly")


    def print_html(self, content):
        '''Helper to pretty-print HTML'''
        content = content.strip()
        if content:
            html = etree.HTML(content)
            print(etree.tostring(html, pretty_print=True, encoding=str))
        else:
            print('<empty content>')