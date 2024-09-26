#!/usr/bin/python3
"""
Unit test cases for the HBNBCommand console.
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        """Set up the HBNBCommand instance for testing."""
        self.hbnb_cmd = HBNBCommand()

    def test_create_command(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_cmd.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output != "" and len(output) == 36)

    def test_show_command(self):
        """Test the show command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_cmd.onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()

            with patch('sys.stdout', new=StringIO()) as mock_stdout_show:
                self.hbnb_cmd.onecmd(f"show BaseModel {instance_id}")
                output = mock_stdout_show.getvalue().strip()
                self.assertIn("BaseModel", output)
                self.assertIn(instance_id, output)

    def test_destroy_command(self):
        """Test the destroy command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_cmd.onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()

            with patch('sys.stdout', new=StringIO()) as mock_stdout_destroy:
                self.hbnb_cmd.onecmd(f"destroy BaseModel {instance_id}")
                output = mock_stdout_destroy.getvalue().strip()
                self.assertEqual(output, "")

                # Verify the instance is truly destroyed
                with patch('sys.stdout', new=StringIO()) as mock_stdout_show:
                    self.hbnb_cmd.onecmd(f"show BaseModel {instance_id}")
                    output_show = mock_stdout_show.getvalue().strip()
                    self.assertIn("** no instance found **", output_show)

    def test_all_command(self):
        """Test the all command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_cmd.onecmd("all BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "[]")  # No instances should be present initially

            # Create an instance to check if it shows up in all
            self.hbnb_cmd.onecmd("create BaseModel")
            with patch('sys.stdout', new=StringIO()) as mock_stdout_all:
                self.hbnb_cmd.onecmd("all BaseModel")
                output_all = mock_stdout_all.getvalue().strip()
                self.assertNotEqual(output_all, "[]")  # Should contain at least one instance

    def test_update_command(self):
        """Test the update command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_cmd.onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()

            # Update with a new attribute
            self.hbnb_cmd.onecmd(
                f"update BaseModel {instance_id} name 'new_name'"
            )

            # Show the instance to verify update
            with patch('sys.stdout', new=StringIO()) as mock_stdout_show:
                self.hbnb_cmd.onecmd(f"show BaseModel {instance_id}")
                output = mock_stdout_show.getvalue().strip()
                self.assertIn("new_name", output)

    def test_help_command(self):
        """Test the help command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_cmd.onecmd("help show")
            output = mock_stdout.getvalue()
            self.assertIn("Prints the string representation of an instance", output)

    def test_class_does_not_exist(self):
        """Test commands for a non-existent class."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_cmd.onecmd("show NonExistentClass")
            output = mock_stdout.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_missing_instance_id(self):
        """Test commands with missing instance id."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_cmd.onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()

            # Attempt to show without ID
            with patch('sys.stdout', new=StringIO()) as mock_stdout_show:
                self.hbnb_cmd.onecmd(f"show BaseModel")
                output = mock_stdout_show.getvalue().strip()
                self.assertIn("** instance id missing **", output)

    def test_destroy_non_existent(self):
        """Test destroying a non-existent instance."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_cmd.onecmd("destroy BaseModel non_existent_id")
            output = mock_stdout.getvalue().strip()
            self.assertIn("** no instance found **", output)

    def test_update_non_existent(self):
        """Test updating a non-existent instance."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_cmd.onecmd("update BaseModel non_existent_id name 'new_name'")
            output = mock_stdout.getvalue().strip()
            self.assertIn("** no instance found **", output)


if __name__ == '__main__':
    unittest.main()
