# ---------- GIORGI BERIDZE ----------
#Lesson 7 home tasks
# Task №1
"""გვაქვს ცარიელი დიქშენერი შევავსოთ 30 შემთხვევითი ელემენტით, 
კეიც და ველიუც უნდა იყოს შემთხვევითი
ყველა ლუწი ქეი უნდა გადავწეროთ ცალკე ლისტში
ყველა კენტი ქეი უნდა გადავწეროთ ცალკე ლისტში
ყველა ლუწი ველიუ უნდა გადავწეროთ ცალკე ლისტში
ყველა კენტი ველიუ უნდა გადავწეროთ ცალკე ლისტში
ეკრანზე გამოიტანოს დიქშენერი და ოთხივე ლისტი"""

import random

dic = {}
odd_key = []
even_key = []
odd_value = []
even_value = []
while len(dic) < 10:
    dic[random.randrange(20,100)]= random.randrange(100,200)
for i,j in dic.items():
    if i % 2 ==0:
        even_key.append(i)
    else:
        odd_key.append(i)
    if j % 2==0:
        even_value.append(j)
    else:
     odd_value.append(j)
print(f"dictionary = {dic}")
print(f"even keys are {len(even_key)} --> {even_key}")
print(f"odd keys are {len(odd_key)} --> {odd_key}")
print(f"even values are {len(even_value)} --> {even_value}")
print(f"odd values are {len(odd_value)} --> {odd_value}")
