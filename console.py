#!/usr/bin/python3
""" HBNBCommand class definition """
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class   the entry point of the command interpreter
    """

    prompt = '(hbnb)'

    __cls = {
        "BaseModel": BaseModel,
        "User": 0,
        "State": 9,
        "City": 4,
        "Place": 9,
        "Amenity": 8,
        "Review": 6
        }

    def emptyline(self):
        """Do nothing if empty line + enter hit"""
        return False

    """-------COMMANDS------"""

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel
                -save it
                -print the id
        """
        line = line.split(' ')
        if not line[0]:
            print('** class name missing **')
        elif line[0] not in __class__.__cls:
            print('** class doesn\'t exist **')
        else:
            instance = __class__.__cls[line[0]]()
            print(instance.id)
            instance.save()

    def do_show(self, line):
        """Prints the string representation of an instance based on:
            - The class name
            - Id
        """
        line = line.split(' ')
        all_instances = storage.all()

        if not line[0]:
            print('** class name missing **')
            return
        elif line[0] not in __class__.__cls:
            print('** class doesn\'t exist **')
            return

        try:
            cls_id = '{}.{}'.format(line[0], line[1])
            if cls_id not in all_instances:
                print('** no instance found **')
            else:
                print(all_instances[cls_id])
        except IndexError:
            print('** instance id missing **')

    def do_destroy(self, line):
        """Deletes an instance based on:
            - The class name
            - Id
        """
        line = line.split(' ')
        all_instances = storage.all()

        if not line[0]:
            print('** class name missing **')
            return
        elif line[0] not in __class__.__cls:
            print('** class doesn\'t exist **')
            return

        try:
            cls_id = '{}.{}'.format(line[0], line[1])
            if cls_id not in all_instances:
                print('** no instance found **')
            else:
                del all_instances[cls_id]
                storage.save()
        except IndexError:
            print('** instance id missing **')

    def do_all(self, line):
        """Prints all string representation of all instances
        """

        all_instances = storage.all()
        li = []
        st = ''
        if line:
            line = line.split(' ')

            if line[0] not in __class__.__cls:
                print('** class doesn\'t exist **')
                return
            else:

                for k in all_instances.values():
                    if k.__class__.__name__ == line[0]:
                        st = str(k)
                        li.append(st)
                print(li)
        else:

            for k in all_instances.values():
                st = str(k)
                li.append(st)

            print(li)

    def do_update(self, argl):
        """Updates an instance based on:
            - The class name
            - Id
        """
        argl = split(argl, ' ')
        all_instances = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__cls:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in all_instances.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        cls_id = "{}.{}".format(argl[0], argl[1])
        obj = all_instances[cls_id]

        if len(argl) == 4:
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            typ = [str, int, float]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in typ):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
