import cmd
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()