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
    
            # Handle the 'update' command with JSON dictionary
            if command == "update":
                # Match for the JSON dictionary format
                if re.fullmatch(r'".*",\s*\{.*\}', params):
                    id_match, json_dict = re.fullmatch(r'"(.*?)",\s*(\{.*\})', params).groups()
                    # Pass the formatted string to do_update
                    self.do_update(f"{class_name} {id_match} {json_dict}")
                else:
                    # Try to parse params as a JSON list
                    try:
                        param_list = json.loads(f"[{params}]")
                    except json.JSONDecodeError:
                        print("** invalid dictionary format **")
                        return
    
                    # Check length of params for required values
                    if len(param_list) < 2:
                        print("** instance id missing **")
                    else:
                        # Handle cases where we have id, attribute name, and value
                        if len(param_list) == 2:
                            print("** attribute name and value missing **")
                        else:
                            # Prepare args for do_update
                            self.do_update(f"{class_name} {param_list[0]} {param_list[1]} {param_list[2]}")
    
            else:
                # Handle other commands: all, count, show, destroy
                if class_name not in self.class_mapping:
                    print("** class doesn't exist **")
                    return
                
                # Handle 'all' command
                if command == "all":
                    self.do_all(class_name)
                elif command == "count":
                    count = sum(1 for key in self.instance_dict if key.startswith(class_name))
                    print(count)
                elif command == "show":
                    if not params:
                        print("** instance id missing **")
                    else:
                        self.do_show(f"{class_name} {params.strip('\"')}")
                elif command == "destroy":
                    if not params:
                        print("** instance id missing **")
                    else:
                        self.do_destroy(f"{class_name} {params.strip('\"')}")
                else:
                    print(f"*** Unknown command: {command}")
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
        key = f"{class_name}.{instance_id}"  # Assuming dot notation for instance key
    
        if key not in self.instance_dict:
            print("** no instance found **")
            return
    
        instance = self.instance_dict[key]
    
        # Check if the third argument is a dictionary
        if len(args) == 3 and args[2].startswith('{') and args[2].endswith('}'):
            try:
                # Parse the dictionary from the input argument
                attributes = json.loads(args[2].replace("'", '"'))
            except json.JSONDecodeError:
                print("** invalid dictionary format **")
                return
    
            # Update the instance attributes using the dictionary
            for attribute_name, attribute_value in attributes.items():
                # You can add extra type checking if needed
                setattr(instance, attribute_name, attribute_value)
    
            instance.save()  # Save after updating
        else:
            # Handle positional attribute update
            if len(args) < 3:
                print("** attribute name missing **")
                return
    
            attribute_name = args[2]
    
            if len(args) < 4:
                print("** value missing **")
                return
    
            try:
                # Try to interpret the value (e.g., convert to int, float, etc.)
                attribute_value = json.loads(args[3].replace("'", '"'))
            except json.JSONDecodeError:
                # If parsing fails, keep the value as a string
                attribute_value = args[3]
    
            # Update the instance with a single attribute and value
            setattr(instance, attribute_name, attribute_value)
            instance.save()  # Save after updating

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
