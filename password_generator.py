import random
import string

# Ask user for password length
while True:
    try:
        length = int(input("Enter desired password length (min 4): "))
        if length >= 4:
            break
        else:
            print("Password length should be at least 4.")
    except ValueError:
        print("Please enter a valid number.")

# Ask if user wants symbols and numbers
include_digits = input("Include numbers? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Create the pool of characters
characters = string.ascii_letters  # a-z and A-Z
if include_digits:
    characters += string.digits
if include_symbols:
    characters += string.punctuation

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

print("\nYour generated password is:", password)
print("Tip: Keep it safe and don't share it with anyone.")
