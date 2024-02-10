#!/usr/bin/python3
"""
Contains the unit test cases for the Place class.
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_instantiation(self):
        """Verify successful instantiation of a Place instance."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        """Check initial attribute values of a Place instance."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attribute_assignment(self):
        """Test attribute assignment to a Place instance."""
        place = Place()

        place.city_id = "789"
        place.user_id = "101"
        place.name = "Cozy Apartment"
        place.description = "A nice place to stay"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["wifi", "parking"]

        self.assertEqual(place.city_id, "789")
        self.assertEqual(place.user_id, "101")
        self.assertEqual(place.name, "Cozy Apartment")
        self.assertEqual(place.description, "A nice place to stay")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["wifi", "parking"])

    def test_to_dict_method(self):
        """Test the to_dict method for correct dictionary output."""
        place = Place()
        place.city_id = "789"
        place.user_id = "101"
        place.name = "Cozy Apartment"
        place.description = "A nice place to stay"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["wifi", "parking"]

        place_dict = place.to_dict()

        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict.get('city_id', ""), "789")
        self.assertEqual(place_dict.get('user_id', ""), "101")
        self.assertEqual(place_dict.get('name', ""), "Cozy Apartment")
        self.assertEqual(place_dict.get('description', ""), "A nice place to stay")
        self.assertEqual(place_dict.get('number_rooms', 0), 2)
        self.assertEqual(place_dict.get('number_bathrooms', 0), 1)
        self.assertEqual(place_dict.get('max_guest', 0), 4)
        self.assertEqual(place_dict.get('price_by_night', 0), 100)
        self.assertEqual(place_dict.get('latitude', 0.0), 37.7749)
        self.assertEqual(place_dict.get('longitude', 0.0), -122.4194)
        self.assertEqual(place_dict.get('amenity_ids', []), ["wifi", "parking"])
        self.assertEqual(place_dict.get('__class__', ""), "Place")

    def test_to_dict_with_empty_attributes(self):
        """
        Test to_dict with a Place instance containing empty attributes.
        """
        place = Place()
        place_dict = place.to_dict()

        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict.get('city_id', ""), "")
        self.assertEqual(place_dict.get('user_id', ""), "")
        self.assertEqual(place_dict.get('name', ""), "")
        self.assertEqual(place_dict.get('description', ""), "")
        self.assertEqual(place_dict.get('number_rooms', 0), 0)
        self.assertEqual(place_dict.get('number_bathrooms', 0), 0)
        self.assertEqual(place_dict.get('max_guest', 0), 0)
        self.assertEqual(place_dict.get('price_by_night', 0), 0)
        self.assertEqual(place_dict.get('latitude', 0.0), 0.0)
        self.assertEqual(place_dict.get('longitude', 0.0), 0.0)
        self.assertEqual(place_dict.get('amenity_ids', []), [])
        self.assertEqual(place_dict.get('__class__', ""), "Place")

    def test_str_representation(self):
        """Check the string representation of a Place instance."""
        place = Place()
        place.city_id = "789"
        place.user_id = "101"
        place.name = "Cozy Apartment"
        place.description = "A nice place to stay"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["wifi", "parking"]

        place_str = str(place)
        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)

        self.assertEqual(place_str, expected_str)

    def test_custom_attributes(self):
        """Test the addition of custom attributes to a Place instance."""
        place = Place()
        place.custom_attribute = "custom_value"

        self.assertTrue(hasattr(place, 'custom_attribute'))
        self.assertEqual(place.custom_attribute, "custom_value")


if __name__ == '__main__':
    unittest.main()
