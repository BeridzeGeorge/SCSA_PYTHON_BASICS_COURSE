# ---------- GIORGI BERIDZE ----------
# Lesson 9 home tasks
# Task №4
"""4. გვაქვს ლისტი, a=["giorgi", "pavle", "mamuka", "dachi","irakli","iago",
"natia", "nino","nika","tamazi" ]პროგრამამ უნდა გადაწეროს ამ ლისტის ელემენტები
დიქშენერში, კეის სახით, ხოლო ველიუები გმოიმუშავოს რენდომულად და მიანიჭოს ქულების
 სახით თითოეულ ელემენტს.
4.1 გავაკეთოტ იგივე ფუნქციით, სადაც პარამეტრად გადავცემთ ლისტს,
ხოლო ველიუებს გამოიმუშავებს ავტომატურად ფუნქციის შიგნით."""

import random

a = ["giorgi", "pavle", "mamuka", "dachi", "irakli", "iago",
     "natia", "nino", "nika", "tamazi"]


def students_points(x_list):
    # Generate random points for students and create corresponding dictionary
    dic = {}
    for i in x_list:
        dic[i] = random.randint(40, 100)
    return dic


print(students_points(a))
