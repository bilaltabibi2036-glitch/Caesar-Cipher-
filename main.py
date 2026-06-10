# Day 8 - Caesar Cipher
# 100 Days of Code Python3

alphabet = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
]
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # If user wants decode, shift goes backward
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        # If it is a normal letter
        if letter in alphabet:
            old_position = alphabet.index(letter)
            new_position = (old_position + shift_amount) % 26
            output_text += alphabet[new_position]

        # If it is space, number, symbol, keep it same
        else:
            output_text += letter

    print(f"\nHere is the {encode_or_decode}d result: {output_text}")


# Program starts here
should_continue = True

while should_continue:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    caesar(
        original_text=text,
        shift_amount=shift,
        encode_or_decode=direction
    )

    restart = input("\nType 'yes' if you want to go again. Otherwise type 'no':\n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye 👋")
