import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars) 
key = chars.copy()

random.shuffle(key) #Shuffle everytinme when ran

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


#Decryption
chipher_text = input("Enter your message to decrypt: ")
text = ""

for letter in chipher_text:
    index = key.index(letter)
    text += chars[index]

print("Decrypted message: ", text)