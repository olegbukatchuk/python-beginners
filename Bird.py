class Bird:
    '''Базовый класс, определяющий состав птиц.'''
    count = 0

    def __init__(self, chat):
        self.sound = chat
        Bird.count += 1

    def talk(self):
        return self.sound
    