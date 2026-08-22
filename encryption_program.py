import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
key = chars.copy()
random.shuffle(key)

user_input = input("Enter a message to encrypt: ")
encrypted_string = ""

if user_input == "":
    print("Please enter a valid input")
    user_input = input("Enter a message to encrypt: ")
else:
    for char in user_input:
        index = chars.index(char)
        encrypted_string += key[index]
    print(encrypted_string)

encrypted_string = input("Enter a message to decrypt: ")
user_input = ""

if encrypted_string == "":
    print("Please enter a valid input")
    encrypted_string = input("Enter a message to encrypt: ")
else:
    for char in encrypted_string:
        index = key.index(char)
        user_input += chars[index]
    print(user_input)
