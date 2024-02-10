#!/usr/bin/python3
"""
Contains unit test cases for the City class.
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_instantiation(self):
        """Verify successful instantiation of a City instance."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """Check initial attribute values of a City instance."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attribute_assignment(self):
        """Test attribute assignment to a City instance."""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_to_dict_method(self):
        """Test the to_dict method for correct dictionary output."""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['state_id'], "CA")
        self.assertEqual(city_dict['name'], "San Francisco")
        self.assertEqual(city_dict['__class__'], "City")

    def test_to_dict_with_empty_attributes(self):
        """Test to_dict with a City instance containing empty attributes."""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict.get('state_id', ""), "")
        self.assertEqual(city_dict.get('name', ""), "")
        self.assertEqual(city_dict['__class__'], "City")

    def test_str_representation(self):
        """Check the string representation of a City instance."""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        city_str = str(city)
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(city_str, expected_str)

    def test_custom_attributes(self):
        """Test the addition of custom attributes to a City instance."""
        city = City()
        city.custom_attribute = "custom_value"
        self.assertTrue(hasattr(city, 'custom_attribute'))
        self.assertEqual(city.custom_attribute, "custom_value")


if __name__ == '__main__':
    unittest.main()
