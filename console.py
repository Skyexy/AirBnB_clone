import cmd
from models.base_model import BaseModel
import re
import models
import sys

class HBNBCommand(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_quit(self, arg):
        sys.exit(1)

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print('EOF command to exit the program')

    def help_quit(self):
        print('Quit command to exit the program')

    def emptyline(self):
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_create(self, arg):
        if not arg:
            print(" ** class name missing ** ")
        elif arg != 'BaseModel':
            print("** class doesn't exist **")
        else:
            model = models.classes[arg]()
            models.storage.new(model)
            models.storage.save()
            print(model.id)

    def do_show(self, arg):
        if arg == "":
            print('** class name missing **')
            return
        try:
            model = models.classes[arg]()
            model_name, model_id = arg.split(' ')
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
        if arg == "":
            print('** class name missing **')
            return
        try:
            model = models.classes[arg]()
            model_name, model_id = arg.split(' ')
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
        if arg == "":
            print([x.__str__() for x in models.storage.all().values()])
        else:
            try:
                model = models.classes[arg]
                resp = []
                for l in models.storage.all().values():
                    if type(l) == model:
                        resp.append(l.__str__())
                print(resp)
            except Exception as e:
                print(e)
    def do_update(self, arg):
        if arg == "":
            print('** class name missing **')
            return
        try:
            model = models.classes[arg]()
            model_name, model_id, attr, value = arg.split(' ')
            print(value)
            value = value.split('"')[1]
            print(value)
            models.storage.update(model_name, model_id, attr, value)
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
        model_name, model_com = line.split('.')
        model = models.classes[model_name]
        if model_com == "all()":
            try:
                class__all = []
                for l in models.storage.all().values():
                    if type(l) == model:
                        class__all.append(l.__str__())
                print(class__all)
            except Exception as e:
                print(e)
        elif model_com == "count()":
            try:
                count = 0
                for l in models.storage.all().values():
                    if type(l) == model:
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
            print(mod1)
            try:
                models.storage.delet(model_name, mod1)
                models.storage.save()
            except Exception as e:
                print(e)
        elif model_com[0:6] == "update":
            mod1 = re.findall(r'\((.*?)\)(?![\'])', model_com)
            mod1 = mod1[0].split('",')
            print(mod1)








if __name__ == '__main__':
    HBNBCommand().cmdloop()