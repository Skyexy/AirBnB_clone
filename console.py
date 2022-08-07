<<<<<<< HEAD
#!/usr/bin/python3
""" console module """
import cmd
from models.base_model import BaseModel
import re
import models
import sys


class HBNBCommand(cmd.Cmd):
    """ cmd for command interpreter """

    def __init__(self):
        """ default """
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

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

    def default(self, line):
        """ do_default: for commands not in others """
        model_name, model_com = line.split('.')
        try:
            model = models.classes[model_name]()
            if model_com == "all()":
                try:
                    class__all = []
                    for dictionary in models.storage.all().values():
                        if type(dictionary) == model:
                            class__all.append(dictionary.__str__())
                    print(class__all)
                except Exception as e:
                    print(e)
            elif model_com == "count()":
                try:
                    count = 0
                    for dictionary in models.storage.all().values():
                        if type(dictionary) == model:
                            count += 1
                    print(count)
                except Exception as e:
                    print(e)
            elif model_com[0:4] == "show":
                mod1 = model_com.split('"')[1]
                try:
                    sho = models.storage.sho(model_name, mod1)
                    print(sho)
                except Exception as e:
                    print(e)
            elif model_com[0:7] == "destroy":
                mod1 = model_com.split('"')[1]
                try:
                    models.storage.delet(model_name, mod1)
                    models.storage.save()
                except Exception as e:
                    print(e)
            elif model_com[0:6] == "update":
                mod1 = re.split(r'\(', model_com)
                print(mod1)
                """""
            try:
                models.storage.update(model_name, modid, attname, attvalue)
                models.storage.save()
            except Exception as e:
                print(e)
                """""
        except Exception as e:
            print(e)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
=======
=======
>>>>>>> 5bca38a3f1c696811b38ca64ab6d85a466cb9579
#!/usr/bin/python3
""" console module """
import cmd
from models.base_model import BaseModel
import re
import models
import sys


class HBNBCommand(cmd.Cmd):
    """ cmd for command interpreter """

    def __init__(self):
        """ default """
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

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

    def default(self, line):
        """ do_default: for commands not in others """
        model_name, model_com = line.split('.')
        try:
            model = models.classes[model_name]()
            if model_com == "all()":
                try:
                    class__all = []
                    for dictionary in models.storage.all().values():
                        if type(dictionary) == model:
                            class__all.append(dictionary.__str__())
                    print(class__all)
                except Exception as e:
                    print(e)
            elif model_com == "count()":
                try:
                    count = 0
                    for dictionary in models.storage.all().values():
                        if type(dictionary) == model:
                            count += 1
                    print(count)
                except Exception as e:
                    print(e)
            elif model_com[0:4] == "show":
                mod1 = model_com.split('"')[1]
                try:
                    sho = models.storage.sho(model_name, mod1)
                    print(sho)
                except Exception as e:
                    print(e)
            elif model_com[0:7] == "destroy":
                mod1 = model_com.split('"')[1]
                try:
                    models.storage.delet(model_name, mod1)
                    models.storage.save()
                except Exception as e:
                    print(e)
            elif model_com[0:6] == "update":
                mod1 = re.split(r'\(', model_com)
                print(mod1)
                """""
            try:
                models.storage.update(model_name, modid, attname, attvalue)
                models.storage.save()
            except Exception as e:
                print(e)
                """""
        except Exception as e:
            print(e)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
