# AirBnB Clone Project

## Project Description

This project is an implementation of a command-line interface (CLI) for an AirBnB clone. The command interpreter will allow users to perform various operations on objects, such as creating, retrieving, updating, and deleting.

## Command Interpreter

The command interpreter is implemented using the Python `cmd` module. It provides a set of commands to interact with and manipulate objects. Users can create new objects, retrieve objects from storage, perform operations, update attributes, and destroy objects.

### How to Start:

To start the command interpreter, run the `console.py` script in the terminal.

    $ ./console.py

### How to Use:

Once the command interpreter is running, use the following commands to manage AirBnB objects:

- `create`: Create a new object (e.g., User, State, City, Place).
- `show`: Retrieve information about a specific object.
- `all`: Display information about all objects or objects of a specific class.
- `update`: Update attributes of a specific object.
- `destroy`: Destroy a specific object.
- `quit`: Exit the command interpreter.

#### Examples

```bash
$ ./console.py
(hbnb) create User
(hbnb) show User 12345
(hbnb) all
(hbnb) update Place 54321 name "New Place"
(hbnb) destroy State 98765
(hbnb) quit

The code uses the pycodestyle (version 2.8.*).
