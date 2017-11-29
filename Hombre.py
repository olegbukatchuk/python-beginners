# -*- coding: utf-8 -*-
from Person import *

class Hombre(Person):
    '''Производный класс.'''

    def speak(self, msg):
        print(self.name, ':\n\tHola!', msg)