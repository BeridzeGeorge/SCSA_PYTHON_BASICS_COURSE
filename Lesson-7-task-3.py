# ---------- GIORGI BERIDZE ----------
#Lesson 7 home tasks
# Task №3
"""შექმენით შემთხვევითი სიტყვა, რომლის სიგრძეც იქნება 7-ის ტოლი.
1.1 შექმენით შემთხვევითი სიტყვა, რომლის სიგრძეც იქნება 2-დან 7-მდე რენდომულად.
1.2 შექმენით შემთხვევითი სიტყვა, რომლის სიგრძეც იქნება 2-დან 7-მდე რენდომულად.  
თუ ამ სიტყვაში აღმოჩნდება სიმბოლო 'a' პროგრამამ დაბეჭდოს ეს სიტყვა, 
ხოლო თუ არ აღმოჩნდება, დაბეჭდოს 'კიდევ სცადეთ'. """
import random
while True:
    rand_word = ""
    temp = ""
    for i in range(random.randint(2,8)):
        rand_word += (chr(random.randint(97,122)))
    if "a" in rand_word:
        print(rand_word.capitalize())
        break
    else:
        temp = input("Press Enter to try again ")

