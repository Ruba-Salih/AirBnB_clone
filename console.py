#!/usr/bin/python3
""" HBNBCommand class definition """
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class   the entry point of the command interpreter
    """

    prompt = '(hbnb)'

    def do_EOF(self):
        exit

    