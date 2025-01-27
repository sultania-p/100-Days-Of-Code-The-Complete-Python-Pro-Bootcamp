## Caesar Cypher Game.. Shifting the letter by some number - Encrypting and Decrypting

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Encrypt Function
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"Here's the encoded result: {cipher_text}")

# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# Decrypt Function
def decrypt(cipher_text, shift_amount):
    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    # e.g.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"Here's the decoded result: {plain_text}")

    # TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable.
    #  You should be able to test the code to encrypt *AND* decrypt a message.

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Invalid input. Please try again!")
