from django.test import TestCase
from account import models as amod
from django.contrib.auth import models as pmod
from datetime import datetime
from lxml import etree

# Create your tests here.
class AccountTests(TestCase):
    fixtures = [ 'account.yaml', 'auth.yaml' ]

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
        u2 = amod.User.objects.get(id=412)
        self.assertEqual(u.first_name, u2.first_name, msg="User not saved correctly")

    def test_permissions_users(self):
        p = pmod.Permission()
        p.codename = 'Djugo'
        p.name = 'Dar jugo'
        p.content_type = pmod.Permission.objects.get(codename='add_user').content_type
        p.save()
        homer = amod.User.objects.get(username='homer')
        homer.user_permissions.add(pmod.Permission.objects.get(codename='Djugo'))
        homer = amod.User.objects.get(username='homer')
        self.assertEqual(homer.has_perm('account.Djugo'), True, msg="User permissions did not set correctly")
    
    def test_permissions_groups(self):
        p1 = pmod.Permission()
        p1.codename = 'fome'
        p1.name = 'Ser fome'
        p1.content_type = pmod.Permission.objects.get(codename='add_user').content_type
        p1.save()
        g1 = pmod.Group()
        g1.name = 'Argentinos'
        g1.save()
        g1.permissions.add(pmod.Permission.objects.get(codename='fome'))
        homer = amod.User.objects.get(username='homer')
        homer.groups.add(pmod.Group.objects.get(name='Argentinos'))
        homer = amod.User.objects.get(username='homer')
        self.assertEqual(homer.has_perm('account.fome'), True, msg='Group permissions not setting correctly')

    def print_html(self, content):
        '''Helper to pretty-print HTML'''
        content = content.strip()
        if content:
            html = etree.HTML(content)
            print(etree.tostring(html, pretty_print=True, encoding=str))
        else:
            print('<empty content>')
