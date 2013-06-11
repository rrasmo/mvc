#!/usr/bin/python

from view import View
from model import Model
from controller import Controller

if __name__ == '__main__':

    view = View()
    controller = Controller()
    model = Model()

    view.setController(controller)
    controller.setModel(model)

    view.cmdloop()

