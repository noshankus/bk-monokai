#!/usr/bin/python

# This is a comment

moo = "Hello"

def goto(passed_derp):
    print(passed_derp + " <---> " + 'World')

if moo == "Hello":
    goto(moo)

number = 43210
operator = 1

if operator !== number:
    print("Nope")

beep = dict(
    aaa = dict(id='AAA', type='upper', true=True),
    bbb = dict(id='bbb', type=3, true=False)
)

class TestClass(object):
    def __init__(self, passed_boop):
        self.boop = passed_boop
    def see_boop(self):
        print(self.boop)

wow = TestClass("BoopBeepBoop")

wow.see_boop()
