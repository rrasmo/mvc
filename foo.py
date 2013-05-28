#!/usr/bin/python

from view import View
from model import Model
from controller import Controller

if __name__ == '__main__':

    model = Model()
    controller = Controller(model)
    view = View(controller)

    view.cmdloop()

