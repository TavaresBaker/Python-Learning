# This program is supposed to display a randomized string of text cooresponding to the same index value in the answers list. I did not want to complicate this as I only wanted to experiment with list indexing and random number generation.
# This was my second project so I started to get much more fancy with the commands I used ie lists.

# To get the random number generator, you will need to import it.

import random

# I gave the name a predetermined value, it was not a necessary detail but added to the quality of the printed text at the end.
# The question is also predetermined but both of these variables could easily be changed to ask for user input. If you want to do it, set name and question equal to str(input("What is your name") or tailor the text in the parenthesis to whatever you need.

name = "Jason"
question = "Am I tall?"

# There were multiple answers I needed to have available and the best way to do this is a list, so I made one named answers and filed it with the potential responses.

answers = [
    'Yes - definitely',
    'It is decidedly so',
    'Without a doubt',
    'Reply hazy, try again',
    'Ask again later',
    'Better not tell you now',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful'
]

# Below is the randomization which is used to index. The random.randint(0, 8) gets a random number which becomes the value of random_number. The random_answer variable is different from the answer list for organization however does not necessarily need to be, you could also just print the list with the index of random number.

random_number = random.randint(0, 8)
random_answer = answers[random_number]

# These print commands are used to display text to the console for humans.

print(f"{name} asks: {question}")
print(f"The Magic Eight Ball says: {random_answer}")
