# ---------- GIORGI BERIDZE ----------
# Lesson 8 home tasks
# Task №4
""" გვაქვს ორი ლისტი. პირველში ჩაწერილია 5 სახელი,
მეორეში 5 ნიშანი. პროგრამამ უნდა შექმნას დიქშენერი,
სადაც სახელები იქნება ქეი, ხოლო ნიშნები იქნება ვალიუ
და თითოეულ სახელს უნდა შეესაბამებოდეს შესაბამისი ნიშანი."""

list_names = ["Edson", "Arantes", "Do", "Nascimento", "Pele"]
list_signs = [1, 2, 3, 4, 10]


def create_dictionary(x, y):
    # create dictionary from two lists.
    new_dict = {}
    for i in range(len(x)):
        new_dict[x[i]] = y[i]
    return new_dict


print(create_dictionary(list_names, list_signs))
