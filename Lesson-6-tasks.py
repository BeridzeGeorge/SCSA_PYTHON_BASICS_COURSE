# ---------- GIORGI BERIDZE ----------
#Lesson 6 home tasks
# Task №1
""" 1. გვაქვს ცარიელი სია პროგრამამ შეგვაყვანინოს 5 სიტყვა, 
პროგრამამ დაბეჭდოს მხოლოდ ის სიტყვები, რომელთა სიგრძეც მეტი იქნება 5-ზე."""
text = []
for i in range(5):
    entered_text = input(f"Enter word N{i+1}: ")
    if len(entered_text) > 5:
        text.append(entered_text)
print(text)

# Task №2
"""2. გვაქვს ორი ტოლი სიგრძის სია, პროგრამამ გაყოს პირველი
 სიის ელემენტები მეორე სიის ელემენტებზე შესაბამისად, 
 როგორც მაგალითზეა  ასახული
  a=[20, 50, 60, 30] b=[4, 5, 6, 10] c=[5,10,10,3] """
a=[20, 50, 60, 30]
b=[4, 5, 6, 10]
c = []
for i in range(len(a)):
    c.append(round(a[i]/b[i]))
print(c)