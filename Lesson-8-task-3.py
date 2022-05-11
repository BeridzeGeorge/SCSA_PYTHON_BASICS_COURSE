# ---------- GIORGI BERIDZE ----------
# Lesson 8 home tasks
# Task №3
""" დაწერეთ ფუნქცია, რომელიც პარამეტრად იღებს დიქშენერს და აბრუნებს ქეიების ტუპლს და ვალუების ტუპლს"""


def dict_to_tuples(x):
    # dictionary to tuples converter, using for loop.
    key_tuple = ()
    value_tuple = ()
    for i, j in x.items():
        key_tuple += (i,)
        value_tuple += (j,)
    return key_tuple, value_tuple

some_dict = {1: "a", 2: "b", 3: "c"}
key_tuple, value_tuple = dict_to_tuples(some_dict)
print(f"dictionary = {some_dict}")
print(f"keys tuple = {key_tuple}")
print(f"values tuple = {value_tuple}")
