# Code to print receipts for a store named "Lovely Loveseats".
# This is my first python project since actually trying to learn it go easy on me.
# This script demonstrates basic variable creation and value assignment.
# While lists could be used, this format is used to focus on individual variables for learning purposes.

# Product 1

lovely_loveseat_description = (
    "Lovely Loveseat. Tufted polyester blend on wood. "
    "32 inches high x 40 inches wide x 30 inches deep. Red or white."
)
lovely_loveseat_price = 254.00

# Product 2

stylish_settee_description = (
    "Stylish Settee. Faux leather on birch. "
    "29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
)
stylish_settee_price = 180.50

# Product 3

luxurious_lamp_description = (
    "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
)
luxurious_lamp_price = 52.15

# Sales tax rate (8.8%)
# Keeping this as a variable makes it easier to update in the future.

sales_tax = 0.088

# Customer 1 purchases: Lovely Loveseat and Luxurious Lamp

customer_one_total = lovely_loveseat_price + luxurious_lamp_price
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# Create a summary of items purchased

customer_one_itemization = lovely_loveseat_description + "\n" + luxurious_lamp_description

# Print itemized receipt

print(customer_one_itemization)
print("\n" + "Customer One Total is:", customer_one_total)
