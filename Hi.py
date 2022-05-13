"""
a = open("C:/Users/Giorgi/Desktop/hi.txt","r")

for i in a:
    if i[0] == "i":
        print(i)
a.close()
a = open("C:/Users/Giorgi/Desktop/hi.txt","r")

for i in a:
    if "e" in i:
        print(i)
a.close()
"""
"""
a = open("C:/Users/Giorgi/Desktop/hi.txt", "r")
b = a.read()
# print(b)
print(b[2:18])
print(len(b))
count_symbols = 0
count_words = 0
count_lines = 1
words = b.split()
print(len(words))
for i in b:
    count_symbols += 1
    if i == " ":
        count_words +=1
    elif i == "\n":
        count_lines +=1
print(count_words)
print(count_lines)
print(count_symbols)
"""

new_file = open("C:/Users/рз/Desktop/hihi.txt","w")
new_file_hihi = new_file.read()

import random
rand_list = []
for i in range(10):
    rand_list.append(random.randint(0,100))
new_file_hihi.write(str(rand_list))
