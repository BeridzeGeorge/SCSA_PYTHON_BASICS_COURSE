# ---------- GIORGI BERIDZE ----------
# Lesson 8 home tasks
# Task №1
"""დაწერეთ ფუნქცია, რომელიც პარამეტრად იღებს ლისტს და გადაყავს ეს ლისტი ტუპლში"""


def list_to_tuple_converter(x):
    # list to tuple converter, using method
    return tuple(x)


print(list_to_tuple_converter([1, 2, "b"]))


def list_to_tuple(x):
    # list to tuple converter, using for loop
    tpl = ()
    for i in x:
        tpl += (i,)
    return tpl


print(list_to_tuple([3, 4, "c"]))
