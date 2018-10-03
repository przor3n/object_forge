# encoding: utf-8
from object_forge.references import ReferenceExpression

class TT1:
    def fun(self, val=None):
        return "This is fun {}".format(val) if val else "This is fun"

class TT2(TT1):
    def asd(self, one, two):
        return "This is {} and this is {}".format(one, two)

class TestReference:
    def test_parsing(self):
        reference_expr = ReferenceExpression()

        env = {
            'robot': "I am a Robot",
            'home': "Hello Honey, I'm Home!",
            're': 'day',
            'er': 'Mr. One',
            'mer': 'Mr. Two',
            'dom': TT1(),
            'rom': TT2()
        }

        exprs = [
            '@robot',
            '@home',
            '@dom.fun()',
            '@rom.fun(@re)',
            '@rom.asd(@er, @mer)'
        ]

        assert env['robot'] == reference_expr.eval(exprs[0], env)
        assert env['home'] == reference_expr.eval(exprs[1], env)
        assert "This is fun" == reference_expr.eval(exprs[2], env)
        assert "This is fun day" == reference_expr.eval(exprs[3], env)
        assert "This is Mr. One and this is Mr. Two" == reference_expr.eval(exprs[4], env)

