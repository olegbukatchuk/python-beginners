# -*- coding: utf-8 -*-
from Person import *

class Man(Person):
    '''Производный класс.'''

    def speak(self, msg ):
        print(self.name, ':\n\tHello!', msg)