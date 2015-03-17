# -*- coding: utf-8 -*-
from tgrocery import Grocery

class Cat:
    def __init__(self):
        self.grocery = Grocery('autohome')

    def test(self):
        print self.grocery.get_load_status()