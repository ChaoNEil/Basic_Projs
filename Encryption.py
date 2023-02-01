import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print("chars: " , chars)
print("key:" , key)

#Enryption
text = input("Enter your message to encrypt: ")
chipher_text = ""

for letter in text:
    index = chars.index(letter)
    chipher_text += key[index]

print("Original message: ", text)
print("Encrypted message: ", chipher_text)