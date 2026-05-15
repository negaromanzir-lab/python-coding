# Final projects of Caesar Cipher project

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "encode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position +shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
            #TODO-3: What happens if the user enters a number/symbol/space?
            #can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
            #eg. start_text = "meet me at 3"
            #end_text = "... .. .. 3"
    print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figer out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. otherwise type 'no'
#If they 'yes' then ask the for direction/text/shift again and call the caesar() function again?
#Hint: Try creating a new function that calls if they type 'yes'

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alpabet?
    #Try running the program and entering a shift number of 45.
    #Hint: Think about you can use the module(%).
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("GoodBye!!!")