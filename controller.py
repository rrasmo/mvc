
class Controller:

    def __init__(self):
        self.x = ''

    def setModel(self, model):
        self.model = model

    def foo(self, params):
        print 'foo in the controller'
        self.model.foo(params)

    def get(self):
        return self.x

    def set(self, val):
        self.x = val

