#!/usr/bin/python3
"""
module for console entry point
"""
import cmd
# import shlex

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
