# ---------- GIORGI BERIDZE ----------
# Lesson 10 class works
# Classes
class FiguraKvadrati():
    def __init__(self, gverdi):
        print("I'm created ")
        self.gverdi = gverdi
    def fartobi(self):
        return "fartobia - " + str(self.gverdi*self.gverdi)
    def perimeter(self):
        return "Permitria - " + str(4*self.gverdi)
kvadrati1 = FiguraKvadrati(8)
print(kvadrati1.fartobi())
print(kvadrati1.perimeter())
#kvadrati2 = FiguraKvadrati(11)
#print(kvadrati2.fartobi(7))

##################
import random


class Listi():
    def __init__(self):
        a = []
        self.a = []
        print(self.a)

    def sheavse(self):
        for i in range(10):
            self.a.append(random.randrange(0, 100))
        return self.a

    def sashualo(self):
        return sum(self.a) / len(self.a)


l1 = Listi()
print(l1.sheavse())
print(l1.sashualo())

l2 = Listi()
print(l2.sheavse())
print(l2.sashualo())

#############

import random


class Listi():
    def __init__(self, a):
        self.a = a
        print(self.a)

    def sashualo(self):
        return sum(self.a) / len(self.a)


l1 = Listi([4, 5, 6, 7])

print(l1.sashualo())

############

