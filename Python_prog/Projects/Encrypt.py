import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key=chars.copy()
random.shuffle(key)
# print(f"chars: {chars}")
# print(f"\nKey: {key}")

#ENCRYPT

plain_text = input("Enter the text to be Encrypted: ")
cypher_text = ""

for letter in plain_text:
  index = chars.index(letter)
  cypher_text += key[index]

print(f"Original Message: {plain_text}")
print(f"Encrypted Message: {cypher_text}")

#----------------------------------------------------------------------------------------

#DECRYPT

cypher_text = input("Enter the text to be Encrypted: ")
plain_text = ""

for letter in cypher_text:
  index = key.index(letter)
  plain_text += chars[index]

print(f"Encrypted Message: {cypher_text}")
print(f"Original Message: {plain_text}")