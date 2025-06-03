# Simple script to check different passwords for strength.
# NOT GREAT SECURITY TO GENUINELY USE IT but for learning to check different values it is great.

# Variables for use within the script. password asks for user input while score is predetermined. You could also give password values but I want my scripts to be more interactive.

password = str(input("Password: \n"))
score = 0

# The following if statements check the password variable for different metrics of strength.

if len(password) >= 8:
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
    score += 1

# This if statement is what calculates your strength rating based on your score.

if score <= 2:
    strength = "Weak"
elif score == 3 or score == 4:
    strength = "Medium"
else:
    strength = "Strong"

# Prints the results of the check, this is the only thing the user sees besides asking for the password.

print(f"Password: {password} | Strength: {strength}")
