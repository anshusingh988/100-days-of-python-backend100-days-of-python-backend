import random
import string

print("🔐 Password Generator")

length = int(input("Enter password length: "))

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

all_chars = letters + digits + special_chars

password = "".join(random.choice(all_chars) for _ in range(length))

print("✅ Generated Password:", password)

