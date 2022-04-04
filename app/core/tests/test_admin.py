from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class setUp(TestCase):

    def setUp(self):
        self.Client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='trevin@gmail.com',
            password='password123'
        )
        self.Client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='trevin@gmail.com',
            password='password123',
            name = 'TEst user full name'
        )

    def test_users_listed(self):
        """Test that users are listed in our page"""
        url = reverse('admin:core_user_changelist')
        res = self.Client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
    

    def test_user_change_page(self):
        """test that the user edit page works"""
        url = reverse('admin:core:user_change',args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code,200)


    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)