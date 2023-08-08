# create a function to encode a message
def caesar_decode(message=input("Please enter a message: "), offset=int(input("Enter the shift number"))):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded_message = ''
    for char in message.lower():
        if char in alphabet:
            index = alphabet.find(char)
            new_index = (index + offset) % 26
            new_char = alphabet[new_index]
            decoded_message+=new_char
        else:
            decoded_message+=char
    return decoded_message

print(caesar_decode())