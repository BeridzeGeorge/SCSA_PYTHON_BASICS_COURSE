# ---------- GIORGI BERIDZE ----------
# Lesson 9 home tasks
# Task №1
"""  1. გვაქვს ორი ლისტი, პირველში არის 5 სახელი, მეორეში 5 ნიშანი.
პროგრამამ უნდა შექმნას დიქშენერი, სადაც სახელებს შეესაბამება key,
 შესაბამისად ნიშნებ შეესაბამება value-ები, ეს დიქშენერი უნდ აჩაიწეროს ფაილში.
1.1. იგივე ამოცანა გააკეთეთ ფუნქციით, სადაც ფუნქცია პარამეტრებად მიიღებს ორივე ლისტს."""


list_names = ["Edson", "Arantes", "Do", "Nascimento", "Pele"]
list_signs = [1, 2, 3, 4, 10]

def create_dictionary(x, y):
    # create dictionary from two lists.
    new_dict = {}
    for i in range(len(x)):
        new_dict[x[i]] = y[i]
    #Creating new txt file and appending some data in it.
    txt_file = open("New_txt_file.txt", 'a')
    for key, value in new_dict.items():
        txt_file.write('%s : %s \n' % (key, value))
    #close file.
    txt_file.close()
    return txt_file
create_dictionary(list_names,list_signs)
