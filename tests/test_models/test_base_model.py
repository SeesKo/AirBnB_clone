#!/usr/bin/python3
"""
Test cases for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import create_autospec


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up a new instance of the BaseModel class before each test."""
        self.model = BaseModel()

    def tearDown(self):
        """Delete the instance of the BaseModel class after each test."""
        del self.model

    def test_instance_creation(self):
        """Verify successful creation of a BaseModel instance."""
        self.assertIsInstance(self.model, BaseModel)

    def test_id_generation(self):
        """Check the generation of the id attribute."""
        self.assertIsNotNone(self.model.id)
        self.assertEqual(len(self.model.id), 36)

    def test_created_at_type(self):
        """Verify the type of the created_at attribute."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """Verify the type of the updated_at attribute."""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """Check the string representation of a BaseModel instance."""
        string_representation = str(self.model)
        self.assertIn("[BaseModel]", string_representation)
        self.assertIn("({})".format(self.model.id), string_representation)

    def test_save_method_updates_updated_at(self):
        """
        Confirm that calling the save method updates the updated_at attribute.
        """
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method to ensure it returns the expected dictionary.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)

    def test_to_dict_method_datetime_format(self):
        """Verify that to_dict returns datetime attributes in string format."""
        model_dict = self.model.to_dict()
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_from_dict_method(self):
        """
        Test the from_dict method to create a new BaseModel instance
        from a dictionary.
        """
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)

    def test_from_dict_method_with_created_at_string(self):
        """Test from_dict with a string representation of created_at."""
        model_dict = self.model.to_dict()
        model_dict['created_at'] = "2022-01-01T12:00:00.000000"
        new_model = BaseModel(**model_dict)
        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, datetime(2022, 1, 1, 12, 0, 0))
        self.assertEqual(new_model.updated_at, self.model.updated_at)

    def test_from_dict_method_with_updated_at_string(self):
        """Test from_dict with a string representation of updated_at."""
        model_dict = self.model.to_dict()
        model_dict['updated_at'] = "2022-01-02T15:30:00.000000"
        new_model = BaseModel(**model_dict)
        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, datetime(2022, 1, 2, 15, 30, 0))

    def test_save_method_calls_storage_save(self):
        """Test that the save method calls the save method of the storage."""
        with unittest.mock.patch('models.storage.save') as mock_save:
            self.model.save()
            mock_save.assert_called_once()

    def test_to_dict_method_includes_additional_attributes(self):
        """Add more attributes to your BaseModel class."""
        self.model.custom_attribute = 'custom_value'
        model_dict = self.model.to_dict()
        self.assertIn('custom_attribute', model_dict)
        self.assertEqual(model_dict['custom_attribute'], 'custom_value')

    def test_str_representation_includes_custom_attributes(self):
        """Add more attributes to your BaseModel class."""
        self.model.custom_attribute = 'custom_value'
        string_representation = str(self.model)
        self.assertIn('custom_attribute', string_representation)
        self.assertIn('custom_value', string_representation)


if __name__ == '__main__':
    unittest.main()
