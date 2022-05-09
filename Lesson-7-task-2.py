# ---------- GIORGI BERIDZE ----------
#Lesson 7 home tasks
# Task №2
""" გვაქვს ცარიელი დიქშენერი
შევავსოთ 20 შემთხვევითი ელემენტით, კეიც და ველიუც უნდა იყოს შემთხვევითი
პროგრამამ გამოიტანოს ქიების საშუალო არითმეტიკული და ვალუების მინიმალური 
და მაქსიმალური მნიშვნელობები."""

import random

dic = {}
dic_key_sum = 0
dic_key_average = 0
dic_value = []

while len(dic) < 10:
    dic[random.randrange(20,100)]= random.randrange(100,200)
    for i,j in dic.items():
        dic_key_sum += i
        dic_value.append(j)
dic_key_average = dic_key_sum / len(dic)

print(f"dictionary = {dic}")
print(f"keys average = {dic_key_average}")
print(f"max value is - {max(dic_value)} \nmin value is - {min(dic_value)}")
print("----------")
