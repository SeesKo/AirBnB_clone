#!/usr/bin/python3
"""
Contains the unit test cases for the Review class.
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_instantiation(self):
        """Verify successful instantiation of a Review instance."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """Check initial attribute values of a Review instance."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attribute_assignment(self):
        """Test attribute assignment to a Review instance."""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great place!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great place!")

    def test_to_dict_method(self):
        """Test the to_dict method for correct dictionary output."""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great place!"
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['place_id'], "123")
        self.assertEqual(review_dict['user_id'], "456")
        self.assertEqual(review_dict['text'], "Great place!")
        self.assertEqual(review_dict['__class__'], "Review")

    def test_to_dict_with_empty_attributes(self):
        """
        Test to_dict with a Review instance containing empty attributes.
        """
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict.get('place_id', ""), "")
        self.assertEqual(review_dict.get('user_id', ""), "")
        self.assertEqual(review_dict.get('text', ""), "")
        self.assertEqual(review_dict['__class__'], "Review")

    def test_str_representation(self):
        """Check the string representation of a Review instance."""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great place!"
        review_str = str(review)
        expected_str = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(review_str, expected_str)

    def test_custom_attributes(self):
        """Test the addition of custom attributes to a Review instance."""
        review = Review()
        review.custom_attribute = "custom_value"
        self.assertTrue(hasattr(review, 'custom_attribute'))
        self.assertEqual(review.custom_attribute, "custom_value")


if __name__ == '__main__':
    unittest.main()
