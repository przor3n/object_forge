# encoding: utf-8
from textx import metamodel_from_str


REFERENCE_SYNTAX = """
Compd: Call | Ref ;
Call: "@" Name=ID "." Function=ID "(" (arguments*=Compd[',']) ")";
Ref: "@" Name=ID;
"""


class Ref:
    def __init__(self, model, env):
        self.env = env
        self.name = model.Name

    def evaluate(self):
        return self.env.get(self.name)

class Call:
    def __init__(self, model, env):
        self.env = env
        self.object = Ref(model, self.env).evaluate()
        self.function = model.Function
        self.arguments = []

        for arg in model.arguments:
            self.arguments.append(Ref(arg, self.env).evaluate())

    def evaluate(self):
        return getattr(self.object, self.function)(*self.arguments)


class ReferenceExpression:
    def __init__(self):
        self.model = metamodel_from_str(REFERENCE_SYNTAX)
        self.tokens = {
            'Ref': Ref,
            'Call': Call,
        }

    def eval(self, text, env):
        output = self.model.model_from_str(text)
        cls = output.__class__.__name__
        return self.tokens.get(cls)(output, env).evaluate()
