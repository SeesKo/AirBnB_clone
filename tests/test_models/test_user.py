#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def test_instantiation(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_assignment(self):
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
        user = User()
        user_dict = user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict.get('email', ""), "")
        self.assertEqual(user_dict.get('password', ""), "")
        self.assertEqual(user_dict.get('first_name', ""), "")
        self.assertEqual(user_dict.get('last_name', ""), "")
        self.assertEqual(user_dict['__class__'], "User")

    def test_str_representation(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        user_str = str(user)
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)

        self.assertEqual(user_str, expected_str)

    def test_custom_attributes(self):
        user = User()
        user.custom_attribute = "custom_value"

        self.assertTrue(hasattr(user, 'custom_attribute'))
        self.assertEqual(user.custom_attribute, "custom_value")

    def test_multiple_instances(self):
        user1 = User()
        user2 = User()

        self.assertNotEqual(user1.id, user2.id)

    def test_default_values(self):
        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
