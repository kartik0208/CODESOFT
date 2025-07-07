
import random
import string

print("Welcome to the Password Generator")

length = int(input("Enter the length of the password: "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

password = "".join(random.choice(all_characters) for _ in range(length))

print("Your generated password is:", password)
