from django.test import TestCase
from django.contrib.auth.models import User

class UserRegistrationTestCase(TestCase):
    def test_user_registration(self):
        # Create a new user
        user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        
        # Verify that the user was created successfully
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('testpassword'))
        
        # Attempt to create another user with the same email address
        with self.assertRaises(Exception):
            User.objects.create_user(
                username='anotheruser',
                email='testuser@example.com',
                password='anotherpassword'
            )
            
        # Attempt to create a user with missing fields
        with self.assertRaises(Exception):
            User.objects.create_user(
                username='missingfieldsuser',
                email='missingfieldsuser@example.com'
            )
