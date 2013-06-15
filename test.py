#!/usr/bin/python

import unittest
from view import View
from controller import Controller 
from model import Model
import mocks

class TestView(unittest.TestCase):

    def setUp(self):
        self.view = View()
        self.view.setController(mocks.MockController())

    def test_do_foo(self):
        self.view.do_foo([])
        self.assertEqual(1, 1)


class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()
        self.controller.setModel(mocks.MockModel())

    def test_foo(self):
        self.controller.foo([])
        self.assertEqual(1, 1)


class TestModel(unittest.TestCase):

    def setUp(self):
        self.model = Model()

    def test_foo(self):
        self.model.foo([])
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

