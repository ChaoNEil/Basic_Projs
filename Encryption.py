import random
import string

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print("chars: " , chars)
print("chars:" , key)