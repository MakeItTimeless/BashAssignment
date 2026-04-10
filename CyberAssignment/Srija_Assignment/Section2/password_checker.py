# Password Strength Checker

import re

password = input("Enter your password: ")

score = 0

# Check length
if len(password) >= 8:
    score += 1
else:
    print("Password should be at least 8 characters long")

# Check uppercase
if re.search("[A-Z]", password):
    score += 1
else:
    print("Add at least one uppercase letter")

# Check lowercase
if re.search("[a-z]", password):
    score += 1
else:
    print("Add at least one lowercase letter")

# Check numbers
if re.search("[0-9]", password):
    score += 1
else:
    print("Add at least one number")

# Check special characters
if re.search("[@#$%^&*!]", password):
    score += 1
else:
    print("Add at least one special character")

# Strength result
print("\nPassword Score:", score)

if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Medium")
else:
    print("Strength: Strong")
