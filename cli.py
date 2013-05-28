
from cmd import Cmd

class Cli(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = '> '

    def do_foo(self, params):
        print 'doing foo'
        print params 

    def help_foo(self):
        print 'foo is foo'

    def do_EOF(self, params):
        print
        return True

    def emptyline(self):
        pass

