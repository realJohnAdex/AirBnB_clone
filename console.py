#!/usr/bin/python3
"""
module for console entry point
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

    def do_quit(self, arg):
        """
        Exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel,
        save it (to the JSON file) and print the id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        elif arg == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        elif arg == "User":
            new_instance = User()
            new_instance.save()
            print(new_instance.id)
        elif arg == "State":
            new_instance = State()
            new_instance.save()
            print(new_instance.id)
        elif arg == "City":
            new_instance = City()
            new_instance.save()
            print(new_instance.id)
        elif arg == "Amenity":
            new_instance = Amenity()
            new_instance.save()
            print(new_instance.id)
        elif arg == "Place":
            new_instance = Place()
            new_instance.save()
            print(new_instance.id)
        elif arg == "Review":
            new_instance = Review()
            new_instance.save()
            print(new_instance.id)
        else:
            pass

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = arg.split(' ')
        if not arg:
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

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = arg.split(' ')
        if not arg:
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

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        args = arg.split(' ')
        if not arg:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items()
                   if args[0] in key])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        args = arg.split(' ')
        if not arg:
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
