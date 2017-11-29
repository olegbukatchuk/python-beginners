# -*- coding: utf-8 -*-
class Person:
    '''Базовый класс.'''

    def __init__(self, name):
        self.name = name

    def speak(self, msg = 'Calling The Base Class'):
        print(self.name, msg)
