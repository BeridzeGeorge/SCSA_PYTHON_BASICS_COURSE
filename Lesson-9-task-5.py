# ---------- GIORGI BERIDZE ----------
# Lesson 9 home tasks
# Task №5
"""5. პროგრამამ მოგვთხოვოს სიტყვის შეყვანა ხუთჯერ და ჩაწეროს შეყვანილი სიტყვა ფაილში
5.1 გავაკეთოთ იგივე ფუნქციით"""


def save_entered_words_into_file(x):
    # save 5 inputted words into file
    txt_file = open(x, "w")
    for i in range(5):
        inputted_words = input(f"Enter word N{i + 1}: ")
        txt_file.write(f'{inputted_words} \n')
    txt_file.close()


save_entered_words_into_file("txt_lesson9_task5.txt")
