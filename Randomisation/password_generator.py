# PASSWORD GENERATOR:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random

num_letter = int(input("Enter how many letters do you want in your password :\n"))
num_numbers = int(input("Enter how many numbers do you want in your password :\n"))
num_symbols = int(input("Enter how many symbols do you want in your password :\n"))
password_list = []
for char in range(1, num_letter+1):
    random_char = random.choice(letters)
    password_list.append(random_char)

for char in range(1, num_numbers+1):
    random_char = random.choice(numbers)
    password_list.append(random_char)

for char in range(1, num_symbols+1):
    random_char = random.choice(symbols)
    password_list.append(random_char)
#print(password_list)    
random.shuffle(password_list)    
#print("Your password is : " , password_list)

password = ""
for char in password_list:
    password = password + char
print(f"Your password is : {password} ")