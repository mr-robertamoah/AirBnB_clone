#!/usr/bin/python3


"""
This module contains the the HBNBCommand class
which implements the cmd.Cmd class
"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """ This is a commandline interpreter for the AirBnB clone """

    def __init__(self):
        """ initialize instance attributes """

        super().__init__()
        self.class_names = [
            "BaseModel", "User",
            "State", "City",
            "Amenity", "Place",
            "Review"
        ]
        self.prompt = "(hbnb) "

    def do_update(self, command):
        """ update command's implementation """

        arguments = command.split(" ")

        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = arguments[0] + "." + arguments[1]
            if key in objects.keys():
                if len(arguments) < 3:
                    print("** attribute name missing **")
                elif len(arguments) < 4:
                    print("** value missing **")
                else:
                    instance = objects[key]
                    value = getattr(instance, arguments[2], None)
                    if value is None:
                        setattr(instance, arguments[2], arguments[3][1:-1])
                    else:
                        value_type = type(getattr(instance, arguments[2]))
                        setattr(instance, arguments[2],
                                value_type(arguments[3][1:-1]))
                    instance.save()
            else:
                print("** no instance found **")

    def help_update(self):
        """ update command's help """

        print('Update command to add or update the attribute of an instance\n'
              'Usage: update <class name> <id> <attribute name> '
              '"<attribute value>"\n')

    def do_all(self, command):
        """ all command's implementation """

        arguments = command.split(" ")

        if arguments[0] != "" and arguments[0] not in self.class_names:
            print("** class doesn't exist **")
        else:
            objects = models.storage.all()
            objects_list = []
            for key, value in objects.items():
                if arguments[0] == "":
                    objects_list.append(str(value))
                    continue

                if arguments[0] == key[:len(arguments[0])]:
                    objects_list.append(str(value))
            print(objects_list)

    def help_all(self):
        """ all command's help """

        print('All command to print a list of all objects\n'
              'Usage: all | all <class name>\n')

    def do_destroy(self, command):
        """ destroy command's implementation """

        arguments = command.split(" ")

        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = arguments[0] + "." + arguments[1]
            if key in objects.keys():
                instance = objects[key]
                models.storage.remove(key)
                models.storage.save()
                del instance
            else:
                print("** no instance found **")

    def help_destroy(self):
        """ destroy command's help """

        print('Destroy command to delete object and remove from file\n'
              'Usage: destroy <class name> <id>\n')

    def do_show(self, command):
        """ show command's implementation """

        arguments = command.split(" ")

        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = arguments[0] + "." + arguments[1]
            if key in objects.keys():
                print(objects[key])
            else:
                print("** no instance found **")

    def help_show(self):
        """ show command's help """

        print('Show command to display string representation of instance\n'
              'Usage: show <class name> <id>\n')

    def do_create(self, command):
        """ create command's implementation """

        if command == "":
            print("** class name missing **")
        elif command not in self.class_names:
            print("** class doesn't exist **")
        else:
            if command == self.class_names[0]:
                instance = BaseModel()
            elif command == self.class_names[1]:
                instance = User()
            elif command == self.class_names[2]:
                instance = State()
            elif command == self.class_names[3]:
                instance = City()
            elif command == self.class_names[4]:
                instance = Amenity()
            elif command == self.class_names[5]:
                instance = Place()
            elif command == self.class_names[6]:
                instance = Review()
            instance.save()
            print(instance.id)

    def help_create(self):
        """ create command's help """

        print('Create command to create an instance of class.\n'
              'Usage: create <class name>\n')

    def do_quit(self, command):
        """ quit command's implementation """

        return True

    def help_quit(self):
        """ quit command's help """

        print('Quit command to exit the program\n')

    def do_EOF(self, command):
        """ EOF command's implementation """

        print()
        return True

    def emptyline(self):
        """ implements what happens when an emptyline is used as command """

        pass

    help_EOF = help_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
