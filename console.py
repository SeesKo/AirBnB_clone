#!/usr/bin/python3
"""
This module contains the HBNBCommand class, the entry
point for the HBNB Command-Line Interface.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
import json


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class provides a command-line interface.
    """

    prompt = "(hbnb) "

    class_mapping = {'BaseModel': BaseModel, 'User': User}
    instance_dict = {}

    # ----- basic commands -----
    def do_create(self, arg):
        """Creates a new instance based on the class name and saves it."""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in self.class_mapping:
            print("** class doesn't exist **")
            return

        new_instance = self.class_mapping[class_name]()
        new_instance.save()
        self.instance_dict[class_name + ' ' + new_instance.id] = new_instance
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.class_mapping:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + ' ' + instance_id
        if key not in self.instance_dict:
            print("** no instance found **")
            return

        print(self.instance_dict[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.class_mapping:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + ' ' + instance_id
        if key not in self.instance_dict:
            print("** no instance found **")
            return

        # Deletion of instance
        del self.instance_dict[key]


    def do_all(self, arg):
        """
        Prints all string representations of instances
        based on the class name or calls the all() method.
        """
        args = arg.split()

        if not args:
            # No class name provided, print all instances of all classes
            instances_list = [str(value) for value in self.instance_dict.values()]
            print(instances_list)
            return

        class_name = args[0]
        if class_name not in self.class_mapping:
            print("** class doesn't exist **")
            return

        # Check if the class has an all() method
        if hasattr(self.class_mapping[class_name], 'all'):
            instances_list = [str(instance) for instance in self.class_mapping[class_name].all()]
            print(instances_list)
        else:
            print("** class doesn't support all() method **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.class_mapping:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + ' ' + instance_id
        if key not in self.instance_dict:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        try:
            # Attempt to cast the attribute value to the correct type
            attribute_value = json.loads(args[3].replace("'", '"'))
        except json.JSONDecodeError:
            print("** invalid value **")
            return

        instance = self.instance_dict[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_help(self, args):
        """Prints help information for the provided command."""
        super().do_help(args)

    def emptyline(self):
        """Executes nothing. Displays a new prompt."""
        pass

    def do_quit(self, args):
        """Exits the command line interface."""
        return True

    def do_EOF(self, arg):
        """Exits the command line interface at end-of-file (EOF)."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
