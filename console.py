#!/usr/bin/python3
"""
This module contains the HBNBCommand class, the entry
point for the HBNB Command-Line Interface.
"""

import re
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import json


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class provides a command-line interface.
    """

    prompt = "(hbnb) "

    class_mapping = {
        'BaseModel': BaseModel,
        'User': User,
        'Amenity': Amenity,
        'City': City,
        'Review': Review,
        'State': State,
        'Place': Place
    }
    instance_dict = {}

    def default(self, arg):
        """
        Handle special cases for commands in dot notation like ClassName.all().
        """
        match = re.fullmatch(r"(\w+)\.(\w+)\((.*?)\)", arg)
    
        if match:
            class_name, command, params = match.groups()
    
            if class_name in self.class_mapping:
                if command in ["all", "count", "show", "destroy"]:
                    # For these commands, we'll use the original logic.
                    param_list = json.loads(f"[{params}]")  # Parsing parameters as list
    
                    if command == "all":
                        self.do_all(class_name)
                    elif command == "count":
                        count = sum(1 for key in self.instance_dict if key.startswith(class_name))
                        print(count)
                    elif command == "show":
                        if not param_list or len(param_list) < 1:
                            print("** instance id missing **")
                        else:
                            self.do_show(f"{class_name} {param_list[0]}")
                    elif command == "destroy":
                        if not param_list or len(param_list) < 1:
                            print("** instance id missing **")
                        else:
                            self.do_destroy(f"{class_name} {param_list[0]}")
                elif command == "update":
                    # Handle update command with JSON dictionary support
                    if re.fullmatch(r'".*",\s*\{.*\}', params):
                        id_match, json_dict = re.fullmatch(r'"(.*?)",\s*(\{.*\})', params).groups()
                        self.do_update(f"{class_name} {id_match} {json_dict}")
                    else:
                        param_list = json.loads(f"[{params}]")
    
                        if not param_list or len(param_list) < 3:
                            if len(param_list) < 2:
                                print("** instance id missing **")
                            elif len(param_list) < 3:
                                print("** attribute name missing **")
                            else:
                                print("** value missing **")
                        else:
                            self.do_update(
                                f"{class_name} "
                                f"{param_list[0]} "
                                f"{param_list[1]} "
                                f"{param_list[2]}"
                            )
                else:
                    print(f"*** Unknown command: {command}")
            else:
                print("** class doesn't exist **")
        else:
            print(f"*** Unknown syntax: {arg}")

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
        key = f"{class_name} {instance_id}"
    
        if key not in self.instance_dict:
            print("** no instance found **")
            return
    
        if len(args) == 3 and args[2].startswith('{') and args[2].endswith('}'):
            # When JSON format is provided
            try:
                attributes = json.loads(args[2].replace("'", '"'))
            except json.JSONDecodeError:
                print("** invalid dictionary format **")
                return
    
            instance = self.instance_dict[key]
            for attribute_name, attribute_value in attributes.items():
                try:
                    # Attempt to cast the attribute value to the correct type
                    attribute_value = json.loads(f'"{attribute_value}"')
                except json.JSONDecodeError:
                    pass
                setattr(instance, attribute_name, attribute_value)
            instance.save()  # Save the updated instance
        else:
            # Traditional update logic
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
                attribute_value = args[3]  # If it fails, keep it as a string
    
            instance = self.instance_dict[key]
            setattr(instance, attribute_name, attribute_value)
            instance.save()  # Save the updated instance

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
