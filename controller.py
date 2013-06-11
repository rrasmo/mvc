
class Controller:

    def __init__(self):
        pass

    def setModel(self, model):
        self.model = model

    def foo(self, params):
        print 'foo in the controller'
        self.model.foo(params)

