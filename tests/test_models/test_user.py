#!/usr/bin/python3
"""
Contains the unit test cases for the User class.
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""
    def test_instantiation(self):
        """Verify successful instantiation of a User instance."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """Check initial attribute values of a User instance."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_assignment(self):
        """Test attribute assignment to a User instance."""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_to_dict_method(self):
        """Test the to_dict method for correct dictionary output."""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        user_dict = user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertEqual(user_dict['__class__'], "User")

    def test_to_dict_with_empty_attributes(self):
        """
        Test to_dict with a User instance containing empty attributes.
        """
        user = User()
        user_dict = user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict.get('email', ""), "")
        self.assertEqual(user_dict.get('password', ""), "")
        self.assertEqual(user_dict.get('first_name', ""), "")
        self.assertEqual(user_dict.get('last_name', ""), "")
        self.assertEqual(user_dict['__class__'], "User")

    def test_str_representation(self):
        """Check the string representation of a User instance."""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        user_str = str(user)
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)

        self.assertEqual(user_str, expected_str)

    def test_custom_attributes(self):
        """
        Test the addition of custom attributes to a User instance.
        """
        user = User()
        user.custom_attribute = "custom_value"

        self.assertTrue(hasattr(user, 'custom_attribute'))
        self.assertEqual(user.custom_attribute, "custom_value")

    def test_multiple_instances(self):
        """
        Verify that multiple User instances have different id values.
        """
        user1 = User()
        user2 = User()

        self.assertNotEqual(user1.id, user2.id)

    def test_default_values(self):
        """Verify default values of a User instance."""
        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
