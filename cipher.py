# create a function to encode a message
def caesar_decode(message,offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded_message = ''
    for char in message.lower():
        if char in alphabet:
            index = alphabet.find(char)
            new_index = index + offset + 1
            #account for numbers greater than 26
            if new_index > 26:
                new_index = new_index%26
            new_char = alphabet[new_index-1]
            decoded_message+=new_char
        else:
            decoded_message+=char
    return decoded_message

#test with an offset of 5
message = "python is fun!"
offset = 5
print(caesar_decode(message,offset))

#test with an offset larger than 26
offset = 29
print(caesar_decode(message,offset))