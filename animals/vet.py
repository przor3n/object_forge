# encoding: utf-8

class Vet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Hi, I'm {}. I'm {} old".format(self.name, self.age)