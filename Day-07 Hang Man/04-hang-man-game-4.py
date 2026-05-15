# step-4
import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False

word_list = ["ardvar", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_len = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f"Pssst, the solutionis {chosen_word}.")

#Create blank
display = []
for _ in range(word_len):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # check guessed letter
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    #TODO-2: - If guess is not a letter in the chosen_word, then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should end and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of lives remaining.
    print(stages[lives])