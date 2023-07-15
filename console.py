#!/usr/bin/python3


"""
This module contains the the HBNBCommand class
which implements the cmd.Cmd class
"""


import cmd
import json
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
                        setattr(
                            instance,
                            arguments[2], arguments[3].replace('"', "")
                        )
                    else:
                        value_type = type(getattr(instance, arguments[2]))
                        setattr(instance, arguments[2],
                                value_type(arguments[3].replace('"', "")))
                    instance.save()
            else:
                print("** no instance found **")

    def get_command(self, command):
        """ reconstruct the command """

        if command.find("(") + 1 == command.find(")"):
            return "{}".format(command[:command.find(".")])

        return "{} {}".format(
            command[:command.find(".")],
            command[command.find(
                "(") + 1:-1].replace('"', '').replace(",", "")
            )

    def onecmd(self, command):
        """ handle commands such as User.all(), User.show(), etc """

        c = command.split(".")
        if len(c) > 1:
            func = command[command.index(".") + 1:command.index("(")]
            if func == "all":
                return self.do_all(command[:command.index(".")])
            elif func == "show":
                return self.do_show(self.get_command(command))
            elif func == "destroy":
                return self.do_destroy(self.get_command(command))
            elif func == "update":
                if command.find("{") >= 0:
                    command_list = command[
                        command.index("{") + 1:command.index("}")
                    ].replace(":", "").split(" ")
                    for i in range(0, len(command_list), 2):
                        new_command = "{} {} {}".format(
                            command[:command.index("{")]
                            .replace('"', '')
                            .replace(", ", "")
                            .replace(".update(", " "),
                            command_list[i].replace("'", "").replace('"', ""),
                            command_list[i + 1]
                            .replace(", ", "").replace(")", "")
                        )
                        self.do_update(self.get_command(new_command))
                    return
                else:
                    return self.do_update(self.get_command(command))
            elif func == "count":
                print(len(self.get_objects(self.get_command(command))))
                return
        return super(HBNBCommand, self).onecmd(command)

    def get_objects(self, arguments):
        """ get the objects in storage """

        objects = models.storage.all()
        objects_list = []
        for key, value in objects.items():
            if arguments[0] == "":
                objects_list.append(str(value))
                continue
            if arguments[0] == key[:len(arguments[0])]:
                objects_list.append(str(value))
        return objects_list

    def do_all(self, command):
        """ all command's implementation """

        arguments = command.split(" ")

        if arguments[0] != "" and arguments[0] not in self.class_names:
            print("** class doesn't exist **")
        else:
            print(self.get_objects(arguments))

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
