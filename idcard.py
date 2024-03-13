from functools import partial
def name():
    msg = ""
    return msg

welcome = partial(name, m)

print(welcome("Josiah"))