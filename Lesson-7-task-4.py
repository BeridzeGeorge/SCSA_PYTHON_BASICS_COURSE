# ---------- GIORGI BERIDZE ----------
#Lesson 7 home tasks
#Task №4
"""შექმენით შემთხვევითი სიტყვა, რომლის სიგრძეც იქნება 2-დან 7-მდე რენდომულად.
თუ ამ სიტყვაში აღმოჩნდება სიმბოლო 'a' ან 'e', პროგრამამ ჩაწეროს ეს სიტყვა ლისტში,
შედეგად მივიღოთ 4 რენდომული სიტყვისგან შემდგარი ლისტი"""
import random
rand_list = []
while len(rand_list) < 4:
    rand_word = ""
    for i in range(random.randint(2,8)):
        rand_word += (chr(random.randint(97,122)))
    if "a" in rand_word or "e" in rand_word:
        rand_list.append(rand_word)
print(rand_list)

