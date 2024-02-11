#!/usr/bin/python3
"""
Contains the unit test cases for the FileStorage class.
"""

import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up a fresh FileStorage instance for each test."""
        self.file_storage = FileStorage()

    def tearDown(self):
        """Clean up the file.json after each test."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_new(self):
        """Test if new() adds the object to __objects."""
        user = User()
        self.file_storage.new(user)
        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertIn(key, self.file_storage.all())

    def test_save_and_reload(self):
        """Test if save() and reload() work together."""
        user = User()
        self.file_storage.new(user)
        self.file_storage.save()

        new_file_storage = FileStorage()
        new_file_storage.reload()

        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertIn(key, new_file_storage.all())
        reloaded_user = new_file_storage.all()[key]
        self.assertIsInstance(reloaded_user, User)
        self.assertEqual(reloaded_user.id, user.id)

    def test_save_multiple_objects(self):
        """Test saving multiple objects to the file."""
        user1 = User()
        user2 = User()
        self.file_storage.new(user1)
        self.file_storage.new(user2)
        self.file_storage.save()

        new_file_storage = FileStorage()
        new_file_storage.reload()

        key1 = "{}.{}".format(user1.__class__.__name__, user1.id)
        key2 = "{}.{}".format(user2.__class__.__name__, user2.id)
        self.assertIn(key1, new_file_storage.all())
        self.assertIn(key2, new_file_storage.all())

    def test_reload_method(self):
        """Test the reload() method."""
        # Create an instance and add an object to it
        user = User()
        self.file_storage.new(user)
        self.file_storage.save()

        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertIn(key, self.file_storage.all())
        reloaded_user = self.file_storage.all()[key]
        self.assertIsInstance(reloaded_user, User)
        self.assertEqual(reloaded_user.id, user.id)

    def test_reload_corrupted_file(self):
        """Test reloading from a corrupted JSON file."""
        # Save an invalid JSON to the file
        with open(FileStorage._FileStorage__file_path, 'w') as file:
            file.write("invalid_json")

        with self.assertRaises(json.JSONDecodeError):
            self.file_storage.reload()

    def test_all(self):
        """Test the all() method."""
        # Create instances of BaseModel and User
        base_model = BaseModel()
        user = User()

        # Add instances to the FileStorage
        self.file_storage.new(base_model)
        self.file_storage.new(user)
        self.file_storage.save()

        # Reload the FileStorage
        new_file_storage = FileStorage()
        new_file_storage.reload()

        # Check if all objects are present in the reloaded FileStorage
        base_model_key = "{}.{}".format(
            base_model.__class__.__name__,
            base_model.id
        )
        user_key = "{}.{}".format(user.__class__.__name__, user.id)

        self.assertIn(base_model_key, new_file_storage.all())
        self.assertIn(user_key, new_file_storage.all())

        # Check the types of the reloaded objects
        reloaded_base_model = new_file_storage.all()[base_model_key]
        reloaded_user = new_file_storage.all()[user_key]

        self.assertIsInstance(reloaded_base_model, BaseModel)
        self.assertIsInstance(reloaded_user, User)

    def test_reload_with_unknown_class(self):
        """Create a JSON file with an unknown class."""
        with open(self.file_storage._FileStorage__file_path, 'w') as file:
            json.dump(
                {'UnknownClass.123': {'id': '123', 'some_attribute': 'value'}},
                file
            )

        # Reload and ensure it doesn't raise an exception or add the object
        self.file_storage.reload()
        self.assertNotIn('UnknownClass.123', self.file_storage.all())

    def test_reload_with_corrupted_json(self):
        """Save an invalid JSON to the file."""
        with open(self.file_storage._FileStorage__file_path, 'w') as file:
            file.write("invalid_json")

        # Ensure reload raises JSONDecodeError
        with self.assertRaises(json.JSONDecodeError):
            self.file_storage.reload()


if __name__ == '__main__':
    unittest.main()
