#!/usr/bin/python3
"""
Contains unit test cases for the Amenity class.
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_instantiation(self):
        """Verify successful instantiation of an Amenity instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Check initial attribute values of an Amenity instance."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attribute_assignment(self):
        """Test attribute assignment to an Amenity instance."""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_to_dict_method(self):
        """Test the to_dict method for correct dictionary output."""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['name'], "Swimming Pool")
        self.assertEqual(amenity_dict['__class__'], "Amenity")

    def test_to_dict_with_empty_attributes(self):
        """
        Test to_dict with an Amenity instance containing empty attributes.
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict.get('name', ""), "")
        self.assertEqual(amenity_dict['__class__'], "Amenity")

    def test_str_representation(self):
        """Check the string representation of an Amenity instance."""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        amenity_str = str(amenity)
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(amenity_str, expected_str)

    def test_custom_attributes(self):
        """Test the addition of custom attributes to an Amenity instance."""
        amenity = Amenity()
        amenity.custom_attribute = "custom_value"
        self.assertTrue(hasattr(amenity, 'custom_attribute'))
        self.assertEqual(amenity.custom_attribute, "custom_value")


if __name__ == '__main__':
    unittest.main()
