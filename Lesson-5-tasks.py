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
    elif count_letter > 5 :
        print("'b'-s are more then expected : ", count_letter)
    elif count_letter < 5:
        print("'b'-s are less then expected : ", count_letter)
    else:
        sum = 0
        for i in range(20):
            sum +=i
        print("sum of numbers from 1 to 20 are: ",sum)
        print("Program ended...")
        break
