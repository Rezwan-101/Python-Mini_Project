import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
print(chars)
key = chars.copy()
random.shuffle(key)

#print(f"Char:{chars}")
#print(f"Key:{key}")


#ENcryption

plain_txt = input("Enter a message to encrypt: ")

chipper_txt = "*# "

for letter in plain_txt:
    index = chars.index(letter)
    chipper_txt += key[index]

print(f"Original Message: {plain_txt}")
print(f"encypt message: {chipper_txt}")


#Decryption

chipper_txt = input("Enter a message to decrypt: ")

plain_txt = "*# "

for letter in chipper_txt:
    index = key.index(letter)
    plain_txt += chars[index]


print(f"encypt message: {chipper_txt}")
print(f"Original Message: {plain_txt}")


#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

