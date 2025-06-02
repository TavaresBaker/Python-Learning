# Ask user for shipping tier and package weight

tier = input('Which tier do you want to go with — "Base" or "Premium"?\n').strip().lower()
weight = float(input("What is the weight of your package?\n"))

# Base shipping rates

if tier == "base":
    if weight <= 2:
        total = 20 + (weight * 1.5)
    elif weight <= 6:
        total = 20 + (weight * 3)
    elif weight <= 10:
        total = 20 + (weight * 4)
    else:
        total = 20 + (weight * 4.75)
    print("Your total comes out to: $", format(total, ".2f"))

# Premium shipping rates

elif tier == "premium":
    if weight <= 2:
        total = weight * 4.5
    elif weight <= 6:
        total = weight * 9
    elif weight <= 10:
        total = weight * 12
    else:
        total = weight * 14.25
    print("Your total comes out to: $", format(total, ".2f"))

# Catch invalid input

else:
    print("Invalid shipping tier. Please choose 'Base' or 'Premium'.")
