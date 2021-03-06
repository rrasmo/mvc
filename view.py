from cmd import Cmd

class View(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = '> '

    def setController(self, controller):
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

    def do_get(self, params):
        print self.controller.get()

    def do_set(self, params):
        if len(params) > 0:
            self.controller.set(params[0])

