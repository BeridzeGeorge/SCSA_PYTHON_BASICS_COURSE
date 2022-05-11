# ---------- GIORGI BERIDZE ----------
# Lesson 8 home tasks
# Task №1
"""დაწერეთ ფუნქცია, რომელიც პარამეტრად იღებს ლისტს და გადაყავს ეს ლისტი ტუპლში"""


def list_to_tuple(x):
    # list to tuple converter, using for loop
    tpl = ()
    for i in x:
        tpl += (i,)
    return tpl


print(list_to_tuple([1, 2, "a"]))


def list_to_tuple_converter(x):
    # list to tuple converter, using method
    return tuple(x)


print(list_to_tuple_converter([3, 4, "b"]))

# Task №2
""" დაწერეთ ფუნქცია, რომელიც პარამეტრად იღებს ტუპლს და გადაყავს ეს ტუპლი ლისტში
"""


def tuple_to_list(x):
    # tuple to list converter, using method
    return list(x)


print(tuple_to_list((5, 6, "c")))


def tuple_to_list_converter(x):
    # tuple to list converter, using for loop
    lst = []
    for i in x:
        lst.append(i)
    return lst


print(tuple_to_list_converter((7, 8, "d")))
