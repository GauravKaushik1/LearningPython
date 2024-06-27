#Guess the Number
import random
import string

target = random.randint(1,5)
print(target)
while True:
    userChoice = int(input("Guess the target or Quit(q): "))
    if(userChoice == "Q"):
        break
    if(userChoice == target):
        
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number was too small. Take a bigger guess..")
    else:
        print("your number was too big. Take a smaller guess.")
print("------Try---Again-------")

'''
Random Password Generator
'''
val = random.choice(["a","b","c","d","e"])
print(val)

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(type(string.ascii_letters))

import random
print(random.choice("hello"))

import random
import string
password_len = 12

charValues = string.ascii_letters + string.digits + string.punctuation
result = "".join([random.choice(charValues) for i in range(password_len)])
#"" contains the joiner to make the list to string
print(result)
result = "".join([random.choice(charValues) for i in range(password_len)])
# password = ""
# for i in range(password_len):
#     password += random.choice(charValues)
print("your password is : ",password)

