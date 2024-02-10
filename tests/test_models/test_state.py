#!/usr/bin/python3
"""
Contains the unit test cases for the State class.
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class."""
    def test_instantiation(self):
        """Verify successful instantiation of a State instance."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """Check initial attribute values of a State instance."""
        state = State()
        self.assertEqual(state.name, "")

    def test_attribute_assignment(self):
        """Test attribute assignment to a State instance."""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_to_dict_method(self):
        """Test the to_dict method for correct dictionary output."""
        state = State()
        state.name = "California"
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['name'], "California")
        self.assertEqual(state_dict['__class__'], "State")

    def test_to_dict_with_empty_attributes(self):
        """
        Test to_dict with a State instance containing empty attributes.
        """
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict.get('name', ""), "")
        self.assertEqual(state_dict['__class__'], "State")

    def test_str_representation(self):
        """Check the string representation of a State instance."""
        state = State()
        state.name = "California"
        state_str = str(state)
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(state_str, expected_str)

    def test_custom_attributes(self):
        """Test the addition of custom attributes to a State instance."""
        state = State()
        state.custom_attribute = "custom_value"
        self.assertTrue(hasattr(state, 'custom_attribute'))
        self.assertEqual(state.custom_attribute, "custom_value")


if __name__ == '__main__':
    unittest.main()
