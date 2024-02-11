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
                self.assertTrue(
                    output != "" and
                    "BaseModel" in output and
                    instance_id in output
                )

    def test_destroy_command(self):
        """Test the destroy command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_cmd.onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()

            with patch('sys.stdout', new=StringIO()) as mock_stdout_destroy:
                self.hbnb_cmd.onecmd(f"destroy BaseModel {instance_id}")
                output = mock_stdout_destroy.getvalue().strip()
                self.assertEqual(output, "")

    def test_all_command(self):
        """Test the all command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_cmd.onecmd("all BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "[]")

    def test_update_command(self):
        """Test the update command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_cmd.onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()

            with patch('sys.stdout', new=StringIO()) as mock_stdout_update:
                self.hbnb_cmd.onecmd(
                    f"update BaseModel {instance_id} name 'new_name'"
                )
                output = mock_stdout_update.getvalue().strip()
                self.assertEqual(output, "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command(self, mock_stdout):
        """Test the help command."""
        with patch('sys.stdin', StringIO('help show\nexit\n')):
            HBNBCommand().cmdloop()
        self.assertIn(
            "Prints the string representation of an instance",
            mock_stdout.getvalue()
        )


if __name__ == '__main__':
    unittest.main()
