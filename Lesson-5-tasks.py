# Lesson 5 home tasks
# Task №1
""" პროგრამამ უნდა შეგვაყვანინოს სტრიქონი და დათვალოს B-ასოების რაოდენობა.
თუ რაოდენობა მეტია ხუთზე - დაწეროს ბევრია და გაჩერდეს, შემდეგ გააგძელოს ახალ ლუპში,
სანამ რაოდენობა ნაკლებია ან ტოლია 5-ზე -ისევ მოგვთხოვოს სტრიქონის შეყვანა,
თუ რაოდენობა ტოლია 5-ის -დათვალოს რიცხვების ჯამი 0-დან 20-მდე და დაასრულოს მუშაობა"""

while True:
    text = input("Enter text  or 'q' to exit the program: ")
    count_letter = text.count("b")
    if text == "q":
        print("Program ended...")
        break
    elif count_letter > 5:
        print("'b'-s are more then expected : ", count_letter)
    elif count_letter < 5:
        print("'b'-s are less then expected : ", count_letter)
    else:
        sum = 0
        for i in range(20):
            sum += i
        print("sum of numbers from 1 to 20 are: ", sum)
        print("Program ended...")
        break
# Lesson 5 task 2
"""
2. პროგრამამ მოგვთხოვოს სახელის შეყვანა, სანამ შეყვანილი სახელის სიგრძე ნაკლები იქნება 2-ზე, დაწეროს"2 ასო მაინც შეიყვანე" და ისევ მოგვთხოვოს სახელის შეყვანა, ასევე, სანამ სახელის სიგრძე მეტია 10-ზე პროგრამამ დაწეროს "ცოტა მოკლედ დაწერე" და ისევ მოგვთხოვოს სახელის შეყვანა, თუ სახელის სიგრძე ეტევა 2-დან 8-მდე დაბეჭდოს ეს სიტყვა და დაასრულოს მუშაობა."""
name = input('Enter the name: ')
while True:
    if len(name) < 2:
        print("Name should contains at least 2 characters")
        name = input("Try again: ")
    elif len(name) > 10:
        print("Too long")
        name = input("Try again with shorter one: ")
    else:
        print(name)
        print("Program ended...")
        break