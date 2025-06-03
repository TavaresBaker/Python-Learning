# This script generates random passwords based on a bunch on differnet words, numbers, and symbols sorted into four different parts. In its current state, it will have the first part follow a theme and the second follow a theme and so on and so forth. if you wanted truly secure passwords, add many more options for all of the sections. add sectiona and break each one down into smaller chunks. I would also reccomend to shuffle the sections around.

import random

#This section is a variety of colors.

first_part = [
    'Red',
    'Orange',
    'Yellow',
    'Green',
    'Blue',
    'Purple',
    'Maroon',
    'Tangerine',
    'Lemon',
    'Lime',
    'Cyan',
    'Violet',
    'Pink',
    'Magenta',
    'Grey',
    'Black',
    'White',
    'Brown',
    'Bronze',
    'Silver',
    'Gold',
    'Plaitnum',
    'Titanium',
    'Copper',
    'Zinc',
    'Alluminum'
]

# The second section is a random 2-digit number.

second_part = list(range(10, 100))

# The third section is a symbol for added security.

third_part = [
    '!',
    '@',
    '#',
    '$',
    '%',
    '^',
    '&',
    '*',
    '(',
    ')',
    '+',
    '='
]

# The last section takes Gen Z slang and adds it in to be pretty random

fourth_part = [
    'Rizzler',
    'Skibidi',
    'Toilet',
    'Jefferey',
    'BigBrain',
    'Rizz',
    'WhatRDose',
    'WhatsUp',
    'Yessir',
    'SkiMask',
    'MikeMyers',
    'Freddy',
    'Mama',
    'Martin',
    'M3M1Z1DaGoats',
]

# To keep everything as random as possible I made a different random variable for each section.

ran_num_one = random.randint(0, 25)
ran_num_two = random.randint(0, 89)
ran_num_three = random.randint(0, 11)
ran_num_four = random.randint(0, 14)

# This prints the results using an f string.

print(f"Your secure password is {first_part[ran_num_one]}{second_part[ran_num_two]}{third_part[ran_num_three]}{fourth_part[ran_num_four]}")














