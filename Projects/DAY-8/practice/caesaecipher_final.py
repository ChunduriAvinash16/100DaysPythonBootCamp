from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift_amount, cipher_direction):
    transferd_text = ''
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            transferd_text += alphabet[new_position%26]
        else:
            transferd_text += letter
    print(f"The {cipher_direction}d text is {transferd_text}")
print(logo)
restart = "yes"
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.")