#!/usr/bin/python3
"""
module for console entry point of the command interpreter
"""
import cmd
# import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# constants
classes = ["BaseModel",
           "User",
           "State",
           "City",
           "Amenity",
           "Place",
           "Review"]


class HBNBCommand(cmd.Cmd):
    """
    Command intetrpreter class
    """
    prompt = "(hbnb) "

    def __init__(self):
        """
        Constructor for HBNBCommand class
        """
        super().__init__()

    def do_quit(self, line):
        """
        Exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

    def do_create(self, line):
        """
        Create a new instance of BaseModel,
        save it (to the JSON file) and print the id.
        """
        if not line:
            print("** class name missing **")
        elif line not in classes:
            print("** class doesn't exist **")
        elif line == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        elif line == "User":
            new_instance = User()
            new_instance.save()
            print(new_instance.id)
        elif line == "State":
            new_instance = State()
            new_instance.save()
            print(new_instance.id)
        elif line == "City":
            new_instance = City()
            new_instance.save()
            print(new_instance.id)
        elif line == "Amenity":
            new_instance = Amenity()
            new_instance.save()
            print(new_instance.id)
        elif line == "Place":
            new_instance = Place()
            new_instance.save()
            print(new_instance.id)
        elif line == "Review":
            new_instance = Review()
            new_instance.save()
            print(new_instance.id)
        else:
            pass

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = line.split(' ')
        if not line:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = line.split(' ')
        if not line:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        args = line.split(' ')
        if not line:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items()
                   if args[0] in key])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        args = line.split(' ')
        if not line:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                setattr(storage.all()[key], args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")

    def default(self, line):
        """
        Default method for command interpreter.
        """
        args = line.split('.')
        if len(args) >= 2:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                count = 0
                for key, value in storage.all().items():
                    if args[0] in key:
                        count += 1
                print(count)
            elif args[1][0:4] == "show":
                new_arg = args[1].split('(')
                new_arg1 = new_arg[1].split(')')
                self.do_show(args[0] + " " + new_arg1[0])
            elif args[1][0:7] == "destroy":
                new_arg = args[1].split('(')
                new_arg1 = new_arg[1].split(')')
                self.do_destroy(args[0] + " " + new_arg1[0])
            elif args[1][0:6] == "update":
                new_arg = args[1].split('(')
                new_arg1 = new_arg[1].split(')')
                new_arg2 = new_arg1[0].split(', ')
                self.do_update(args[0] + " " + new_arg2[0] + " " + new_arg2[1] + " " + new_arg2[2])
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
