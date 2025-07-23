# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-1: create encode method
# TODO-2: create decode method
# TODO-3: What happens if the user enters a number/symbol/space?
def decrypt(original_text, shift_amount):
    decipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position= alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            decipher_text += alphabet[shifted_position]
        else:
            decipher_text += letter
    print(f"Here is the encoded result: {decipher_text }")

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")

def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "decode":
        decrypt(original_text, shift_amount)
    else:
        encrypt(original_text, shift_amount)


# TODO-4: Can you figure out a way to restart the cipher program?

should_continue = True


while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False


