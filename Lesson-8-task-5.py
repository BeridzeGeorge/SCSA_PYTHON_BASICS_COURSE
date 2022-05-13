# ---------- GIORGI BERIDZE ----------
# Lesson 8 home tasks
# Task №5
"""  გვაქვს 20 ელემენტისგან შემდგარი რიცხვების დიქშენერი,
პროგრამამ ყველა ლუწი ქეი უნდა ჩაწეროს ცალკე ლისტში,
ყველა კენტი ქეი უნდა ჩაწეროს ცალკე ლისტში, ყველა ლუწი
ვალიუ უნდა ჩაწეროს ცალკე ლისტში, ყველა კენტი ვალიუ
უნდა ჩაწეროს ცალკე ლისტში,
5.1 იგივე ამოცანა გააკეთეთ ფუნქციით, სადაც პარამეტრის
სახით გადავა დიქშენერი."""
import random

dic = {}
odd_key = []
even_key = []
odd_value = []
even_value = []
while len(dic) < 10:
    # Creating dictionary with randomly generated numbers
    dic[random.randrange(20, 100)] = random.randrange(100, 200)

def dict_to_odd_even_lists(x):
    # Splitting dictionary into lists with odd and even numbers
    for i, j in dic.items():
        if i % 2 == 0:
            even_key.append(i)
        else:
            odd_key.append(i)
        if j % 2 == 0:
            even_value.append(j)
        else:
            odd_value.append(j)
    return even_key, odd_key, even_value, odd_value


# Separating returned tuple into corresponding lists
even_key, odd_key, even_value, odd_value = dict_to_odd_even_lists(dic)
print(f"dictionary = {dic}")
print(f"even keys are {len(even_key)} --> {even_key}")
print(f"odd keys are {len(odd_key)} --> {odd_key}")
print(f"even values are {len(even_value)} --> {even_value}")
print(f"odd values are {len(odd_value)} --> {odd_value}")
