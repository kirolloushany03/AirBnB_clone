#!/usr/bin/python3

"""A command-line interface module for managing instances of
classes in the HBNB project.

This module provides a command-line interface (CLI) for
interacting with instances of various classes such as State,
City, Amenity, Place, Review, BaseModel, and User in the HBNB
project.

Classes:
    HBNBCommand: A class representing the command interpreter
    for the HBNB project.

Functions:
    split_cury: A function to extract ID and dictionary from an
    extra command.

Attributes:
    prompt (str): The prompt displayed for user input in the
    command-line interface.

Usage:
    To run the CLI, execute this module as the main program:
        $ python hbnb_cli.py

    After running the CLI, you can use commands like 'all',
    'show', 'create', 'destroy', 'update', and custom commands
    to manage instances of different classes in the HBNB project.

Example:
    $ python hbnb_cli.py
    (hbnb) all State
    [State<id>, State<id>, ...]
    (hbnb) create User
    <created_user_id>
    (hbnb) show User <user_id>
    User<id>: {'attribute': 'value', ...}
    (hbnb) destroy User <user_id>
    (hbnb) update User <user_id> name "John Doe"
    (hbnb) quit

Note:
    This module assumes the existence of other modules and classes
    from the HBNB project, including 'storage', 'State', 'City',
    'Amenity', 'Place', 'Review', 'BaseModel', and 'User'.
    Ensure that these dependencies are properly set up before
    running this module.

"""


import cmd
import re
import shlex
import ast
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models.user import User


def split_cury(extra_command):
    """Extracts ID and dictionary from extra command.

    Args:
        extra_command (str): Extra command provided.

    Returns:
        tuple: A tuple containing ID and dictionary extracted from the command.
        Returns None if argument is missing or dictionary format is invalid.
    """
    curly_braces = re.search(r"\{(.*?)\}", extra_command)

    if curly_braces:
        id_with_comma = shlex.split(extra_command[: curly_braces.span()[0]])
        id = [i.strip(",") for i in id_with_comma]

        str_data = curly_braces.group(1)

        try:
            arg_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("** invalid dictionary format **")
            return None

        return id, arg_dict
    else:
        print("** argument missing **")
        return None


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""  # \n
        return True

    def help_quit(self):
        """Quit command to exit the program"""
        print("Quit command to exit the program.")

    def do_EOF(self, args):
        """EOF signal to exit the program"""
        print()
        return True

    def help_EOF(self):
        """EOF signal to exit the program"""
        print("EOF signal to exit the program.")

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    @staticmethod
    def checkargs(args, num):
        """Checks and validates the provided arguments.

        Args:
            args (str): Arguments provided.
            num (int): Expected number of arguments.

        Returns:
            list: List of arguments split by space.

        Raises:
            ValueError: If class name is missing,
            class doesn't exist, or instance ID is missing.
        """
        arg = args.split()
        if not arg:
            # raise ValueError("** class name missing **")
            return print("** class name missing **")
        class_name = arg[0]
        cls = storage.get_class(class_name)
        if cls is None:
            # raise ValueError("** class doesn't exist **")
            return print("** class doesn't exist **")
        if num == 2 and len(arg) < 2 and cls:
            # raise ValueError("** instance id missing **")
            return print("** instance id missing **")
        return arg

    def do_create(self, args):
        """create command to Creates a new instance and prints the id"""
        cls = self.checkargs(args, 1)
        if cls:
            name = cls[0]
            cls = storage.get_class(name)
        if cls:
            new_instance = cls()
            new_instance.save()
            print(new_instance.id)

    def help_create(self):
        """create command to Creates a new instance and prints the id"""
        print("create command to Creates a new instance and prints the id")

    def do_show(self, args):
        """Prints the string representation of\
            an instance based on the class name and id
        """
        cls = self.checkargs(args, 2)
        if cls:
            classname, inistanceid = cls
            objs = storage.all()
            key = f"{classname}.{inistanceid}"
            obj = objs.get(key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def help_show(self):
        """Prints the string representation of\
            an instance based on the class name and id"""
        print(
            "Prints the string representation of "
            "an instance based on the class name and id"
        )

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        cls = self.checkargs(args, 2)
        if cls:
            classname, inistanceid = cls
            objs = storage.all()
            key = f"{classname}.{inistanceid}"
            obj = objs.get(key)
            if obj is None:
                print("** no instance found **")
            else:
                del objs[key]
                storage.save()

    def help_destroy(self):
        """Deletes an instance based on the class name and id"""
        print("Deletes an instance based on the class name and id")

    def do_all(self, args):
        """Prints all string representation of\
            all instances based or not on the class name
        """
        if not args:
            print([str(value) for value in storage.all().values()])
        else:
            cls_name = self.checkargs(args, 1)
            if cls_name is None:
                print("** class doesn't exist **")
                return

            all_objs = storage.all()
            class_objs = []
            # class_objs.append(cls_name)
            for value in all_objs.values():
                if value.__class__.__name__ == cls_name[0]:
                    class_objs.append(str(value))

            print(class_objs)

    def help_all(self):
        """Prints all string representation of\
            all instances based or not on the class name"""
        print(
            "Prints all string representation of "
            "all instances based or not on the class name"
        )

    def default(self, arg):
        """Handles custom commands."""
        try:
            args_list = arg.split(".")  # user  all()
            cls_name = args_list[0]

            command = args_list[1].split("(")
            incom_method = command[0]

            extra_command = command[1].split(")")[0].strip()

            dic = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update,
                "create": self.do_create,
            }
            if incom_method == "count":
                return self.do_count(cls_name)

            if incom_method == "show":
                instance_id = command[1].strip(")").strip('"')
                return self.do_show(f"{cls_name} {instance_id}")

            if incom_method == "destroy":
                instance_id = command[1].strip(")").strip('"')
                return self.do_destroy(f"{cls_name} {instance_id}")

            # if incom_method == "create":
            #     return self.do_create(f"{cls_name}")

            if incom_method == "update":
                all_args = [
                    arg.strip().strip('"') for arg in extra_command.split(",")
                ]
                if len(all_args) != 3:
                    print("** Incorrect number of arguments for update **")
                    return False
                obj_id, attribute_name, attribute_value = all_args
                [obj_id], arg_dict = split_cury(extra_command)

                try:
                    if isinstance(arg_dict, str):
                        attributes = arg_dict
                        return self.do_update(
                            f"{cls_name} {obj_id} \
                                            {attribute_name} {attribute_value}\
                                                {attributes}"
                        )
                    elif isinstance(arg_dict, dict):
                        dict_attributes = arg_dict
                        return self.do_update(
                            f"{cls_name} \
                                            {obj_id} {dict_attributes}"
                        )
                except Exception:
                    print("** argument missing**")

            if incom_method in dic.keys():
                return dic[incom_method]("{} {}".format(cls_name, ""))

        except Exception:
            # print(f"*** Unknown syntax: {arg}")
            print(f"** command not found **")
            return False

    def do_count(self, cls_name):
        """Prints the number of all string representation of\
            all instances based or not on the class name"""
        count = 0
        for instance in storage.all().values():
            if instance.__class__.__name__ == cls_name:
                count += 1
        print(count)

    def help_count(self):
        """Prints the number of all string representation of\
            all instances based or not on the class name"""
        print(
            "Prints the number of all string representation of "
            "all instances based or not on the class name"
        )

    def do_update(self, args):
        """Updates an instance based on the class name\
            and id by adding or updating attribute"""
        try:
            arg = self.checkargs(args, 2)
            if len(arg) < 3:
                print("** Insufficient arguments **")
                return

            class_name = arg[0]
            instance_id = arg[1]
            attribute_dict_str = " ".join(arg[2:])

            objs = storage.all()
            key = f"{class_name}.{instance_id}"
            if key not in objs:
                print("** No instance found **")
                return

            obj = objs[key]

            attribute_dict = ast.literal_eval(attribute_dict_str)

            for attr_name, attr_value in attribute_dict.items():
                setattr(obj, attr_name, attr_value)

            obj.save()
        except ValueError:
            print("** Invalid dictionary format **")
        except Exception as e:
            print(f"Error: {e}")

    def help_update(self):
        """Updates an instance based on the class name\
            and id by adding or updating attribute"""
        print(
            "Updates an instance based on the class name "
            "and id by adding or updating attribute"
        )


if __name__ == "__main__":
    HBNBCommand().cmdloop()
