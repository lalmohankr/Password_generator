import random
import string

print("Welcome to the password genertor tool.")
length = input("Enter the length of the password: ")
if length.isdigit():
    length = int(length)
else:
    print("Enter the number only...!!")
    quit()

quan = input("Enter the quantity of the password: ")
if quan.isdigit():
    quan = int(quan)
    passwords = quan
else:
    print("Enter the number only...!!")
    quit()


while (quan > 0):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbol = string.punctuation

    all = lower + upper + num + symbol
    temp = random.sample(all,length)
    password = "".join(temp)
    print(password)
        
    quan -= 1

print(" ")
print(passwords, "password generated successfully.")
print("Thank you!!!")