# step-1
import random

word_list = ["ardvar", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase

guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guess is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter in guess:
        print("Right")
    else:
        print("Wrong")