# encoding: utf-8

class Animals(object):
    def __init__(self, sound):
        self.sound = sound

    def speak(self):
        return self.sound