# ---------- GIORGI BERIDZE ----------
# Lesson 10 class works
# Try-except
"""
try:
    a=int(input("sheiyvane ricxvi"))
    b=int(input("sheiyvane ricxvi"))

    print(a/b)

except:
    print("ragac shecdoma gaipara")
print("programa agrzelebs mushaobas")
"""
"""
try:
    a = int(input("Enter a number "))
    b = int(input("Enter a number "))
    c = (a/b)
except ZeroDivisionError as sh:
    print("Zero division is not allowed! " + str(sh))
except ValueError as sh:
    print("Enter only number! "+ str(sh))
except:
    print("Something wrong has happened")
else:
    print(c)
finally:
    print("Code continues work")
"""

"""
a = [3,9,6,8]
b = [1,3,0,4]
c = []
for i in range(len(a)):
    try:
        c.append(a[i]/b[i])
    except ZeroDivisionError as sh:
        print("Division by zero is not allowed! " + str(sh))
        c.append("Error")
print("Code continues work")
print(c)
"""