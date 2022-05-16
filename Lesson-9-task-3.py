# ---------- GIORGI BERIDZE ----------
# Lesson 9 home tasks
# Task №3
"""3. გვაქვს 20 ელემენტისგან შემდგარი რიცხვების დიქშენერი,
პროგრამამ ყველა ლუწი ქეი უნდა ჩაწეროს ცალკე ტუპლში,
ყველა კენტი ქეი უნდა ჩაწეროს ცალკე ლისტში,
ყველა ლუწი ვალიუ უნდა ჩაწეროს ცალკე ლისტში,
ყველა კენტი ვალიუ უნდა ჩაწეროს ცალკე ტუპლში.
ორივე ტუპლი უნდა ჩაიწეროს ფაილში.
3.1 იგივე ამოცანა გააკეთეთ ფუნქციით, სადაც დიქშენერი გადავა პარამეტრის სახით."""
import random
dic = {}

while len(dic) < 10:
    # Creating dictionary with randomly generated numbers
    dic[random.randrange(20, 100)] = random.randrange(100, 200)
txt_file = open("txt_lesson9_task3.txt", "w")
for key, value in dic.items():
    txt_file.write('%s : %s \n' % (key, value))


def dict_to_odd_even_lists(x):
    odd_key = []
    even_key = ()
    odd_value = []
    even_value = ()
    # Splitting dictionary into lists with odd and even numbers
    for i, j in x.items():
        if i % 2 == 0:
            even_key += (i,)
        else:
            odd_key.append(i)
        if j % 2 == 0:
            even_value += (j,)
        else:
            odd_value.append(j)
    # adding split dictionary data to the file
    txt_file.write('even keys --> %s \nodd keys --> %s \neven values --> %s  \nodd values --> %s  \n'
                   % (even_key, odd_key, even_value, odd_value))
    txt_file.close()


dict_to_odd_even_lists(dic)