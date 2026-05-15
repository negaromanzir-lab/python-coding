# step-2
import random
word_list = ["ardvar", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f"Pssst, the solutionis {chosen_word}.")

#TODO-1 - Create an empty list called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_len = len(chosen_word)

for _ in range(word_len):
    display += "_"

guess = input("Guess a letter: ").lower()

#TODO-2 - Loop through each position in the chosen_word;
# if the letter at that position matches 'guess' then reaveal that letter in the display at tha position.
#e.g. If the user guessed "p" and the chosen word was "apple", then user display should be ["_", "p", "p", "_", "_"]
for position in range(word_len):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

#TODO-3: - print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_"
#Hins - Don't worry about getting the user to guess to guess the next letter. we'll tackle the in step 3.
print(display)