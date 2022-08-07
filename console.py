#!/usr/bin/python3
""" console module """
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return 
    
    
    
class HBNBCommand(cmd.Cmd):
    """ cmd for command interpreter """
    prompt = '(hbnb) '
    
    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """ quit """
        sys.exit(1)

    def do_EOF(self, line):
        """ EOF """
        return True

    def help_EOF(self):
        """ help_EOF """
        print('EOF command to exit the program')

    def help_quit(self):
        """ help_quit """
        print('Quit command to exit the program')
    
    def help_create(self):
        """ help_EOF """
        print('create cinstances of a class')

    def emptyline(self):
        """ empty_line overrider """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_create(self, arg):
        """ do_create create new class instance """
        if not arg:
            print(" ** class name missing ** ")
        else:
            try:
                model = models.classes[arg]()
                models.storage.new(model)
                models.storage.save()
                print(model.id)
            except Exception as e:
                print(e)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_show(self, arg):
        """ do_show: show objects of a instance """
        if arg == "":
            print('** class name missing **')
            return
        else:
            try:
                model_name, model_id = arg.split(' ')
                models.classes[model_name]()
                model = models.storage.sho(model_name, model_id)
                print(model)
            except Exception as e:
                if arg.count(' ') > 1:
                    print("** too many arguments (2 arguments required)**")
                elif arg.count(' ') == 0:
                    print("** instance id missing **")
                else:
                    print(e)

    def do_destroy(self, arg):
        """ do_destroy: destroy a instance"""
        if arg == "":
            print('** class name missing **')
            return
        else:
            try:
                model_name, model_id = arg.split(' ')
                models.classes[model_name]()
                models.storage.delet(model_name, model_id)
                models.storage.save()
            except Exception as e:
                if arg != BaseModel:
                    print("** class doesn't exist **")
                elif arg.count(' ') > 1:
                    print("** too many arguments (2 arguments required)**")
                elif arg.count(' ') == 0:
                    print("** instance id missing **")
                else:
                    print(e)

    def do_all(self, arg):
        """ do_all: show all objects """
        if arg == "":
            print([x.__str__() for x in models.storage.all().values()])
        else:
            try:
                model = models.classes[arg]
                resp = []
                for dictionary in models.storage.all().values():
                    if type(dictionary) == model:
                        resp.append(dictionary.__str__())
                print(resp)
            except Exception as e:
                print(e)

    def do_update(self, arg):
        """ do_update: update a instance with attr and value """
        if arg == "":
            print('** class name missing **')
            return
        else:
            try:
                value = arg.split(' ')
                model_name = value[0]
                model_id = value[1]
                attr = value[2]
                value1 = value[3]
                models.classes[model_name]()
                value1 = value1.split('"')[1]
                models.storage.update(model_name, model_id, attr, value1)
                models.storage.save()
            except Exception as e:
                if arg.count(' ') == 0:
                    print("** instance id missing **")
                elif arg.count(' ') == 1:
                    print("** attribute name missing **")
                elif arg.count(' ') == 2:
                    print("** value missing **")
                else:
                    print(e)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
