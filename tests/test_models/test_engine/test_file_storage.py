#!/usr/bin/python3
"""
Contains the unit test cases for the FileStorage class.
"""

import unittest
import os
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

        """Create a new FileStorage instance to simulate program restart."""
        new_file_storage = FileStorage()
        new_file_storage.reload()

        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertIn(key, new_file_storage.all())
        reloaded_user = new_file_storage.all()[key]
        self.assertIsInstance(reloaded_user, User)
        self.assertEqual(reloaded_user.id, user.id)


if __name__ == '__main__':
    unittest.main()
