#!/usr/bin/python

# This is a comment
# Missing syntax highlighting:
# 1) equals sign is not included in operators, while only the exclamation mark of != is...
# 2) "in" and "not" are defined as "cm-keyword"
# 2) "if", "in" and "not" are defined as "cm-keyword", just like "def" - perhaps a "cm-keyword-2" might be appropriate?
# 3) custom functions are identified as variables (see goto())
# 4) classes during instantiation are identified as variables - poor readability
# 5)

moo = "Hello"

def goto(passed_derp):
    print(passed_derp + " <---> " + 'World')

if moo == "Hello":
    goto(moo)
if moo != "Hello":
    goto(moo)

ccc = None

number = 43210
text_operators = list(1, 32, 43210)

if number not in text_operators:
    print("Nope")

beep = dict(
    aaa = dict(
        id   = 'AAA',
        type = 'upper',
        true = True
    ),
    bbb = {
        "id":   'bbb',
        "type": 3,
        "true": False
    }
)

print(beep.aaa.id)
print(beep.bbb.id)


class TestClass(object):
    def __init__(self, passed_boop):
        self.boop = passed_boop
    def see_boop(self):
        print(self.boop)

wow = TestClass("BoopBeepBoop")

wow.see_boop()
