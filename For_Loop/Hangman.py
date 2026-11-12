# HANGMAN PROBLEM

import random
#Todo1 Randomly choose a word from word_list and assign it to a variable called chosen_word.Then print it.
#Todo2 Ask a user to guess a letter and assign the letter to the variable "guess".Make guess lowercase
#Todo3 Check if the letter the user used is (guess) is one of the letter in the chosen_word. If yes print Right if no print Wrong



word_list = [ "tanmay" , "sunnydeol" , "johncena"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for position in range(1 , len(chosen_word)):
    placeholder += "-"
print(placeholder)    

guess = input("Choose a letter : ").lower()


display = ""
for letter in chosen_word:
    if letter == guess :
        display += letter
    else:
        display += "_"   
print(display)        