
from cmd import Cmd

class View(Cmd):

    def __init__(self, controller):
        Cmd.__init__(self)
        self.prompt = '> '
        self.controller = controller

    def do_foo(self, params):
        print 'foo in the view'
        self.controller.foo(params)

    def help_foo(self):
        print 'foo is foo'

    def do_EOF(self, params):
        print
        return True

    def emptyline(self):
        pass
