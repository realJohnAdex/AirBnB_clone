#!/usr/bin/python3
"""
module for console entry point
"""
import cmd
# import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command intetrpreter class
    """
    prompt = "(hbnb) "

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
        elif arg not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif arg == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        else:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
