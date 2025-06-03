# --- Pizza Menu Setup ---

# List of available toppings
toppings = [
    "pepperoni",
    "pineapple",
    "cheese",
    "sausage",
    "olives",
    "anchovies",
    "mushrooms"
]

# Corresponding prices for each topping
prices = [
    2,
    6,
    1,
    3,
    2,
    7,
    2
]

# Combine prices and toppings into a single list
# I just learned today a way to combine both lists, I hard coded this for no reason. Once I have a script on this repository that shows what im talking about I will update this comment with the name and line #.
pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

# --- Basic Stats ---

# Count how many pizzas cost $2
num_two_dollar_slices = prices.count(2)

# Total number of different pizzas
num_pizzas = len(toppings)

# Output stats
print("Number of $2 slices:", num_two_dollar_slices)
print("We sell", num_pizzas, "different kinds of pizza!")

# --- Sort and Update Pizza List ---

# Sort pizzas by price (ascending)
pizza_and_prices.sort()
print("\nSorted Pizza List (Lowest to Highest Price):")
print(pizza_and_prices)

# Identify cheapest and most expensive pizzas
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

# Remove the most expensive pizza
pizza_and_prices.pop()

# Add a new pizza in the correct sorted position
pizza_and_prices.insert(4, [2.5, "peppers"])
print("\nUpdated Pizza List After Adding 'peppers':")
print(pizza_and_prices)

# Get the three cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print("\nThree Cheapest Pizzas:")
print(three_cheapest)
