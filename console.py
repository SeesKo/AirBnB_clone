#!/usr/bin/python3
"""
This module contains the HBNBCommand class, the entry
point for the HBNB Command-Line Interface.
"""

import cmd
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class provides a command-line interface.
    """

    intro = ("Welcome to the HBNB Command Line Interface.\n"
             "Type 'help' for more commands.\n")
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
        """Prints all string representations of all instances."""
        args = arg.split()
        instances_list = []

        if not args:
            for key, value in self.instance_dict.items():
                class_name, _ = key.split()
                if class_name in self.class_mapping:
                    instances_list.append(str(value))
            print(instances_list)
            return

        class_name = args[0]
        if class_name not in self.class_mapping:
            print("** class doesn't exist **")
            return

        for key, value in self.instance_dict.items():
            if key.startswith(class_name):
                instances_list.append(str(value))

        print(instances_list)

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

        attribute_value_str = args[3]
        attribute_value = None

        try:
            # Attempt to cast the attribute value to the correct type
            attribute_value = eval(attribute_value_str)
        except TypeError:
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
