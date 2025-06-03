import random 

# Static category pools
special_characters = [
"!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
"-", "_", "+", "=", "{", "}", "[", "]", "|",
":", ";", "'", "<", ">", ",", ".", "?", "/",
"`", "~"
]      
numbers = [str(num) for num in range(10, 100)]
verbs = []
adjectives = []
colors = []
statics = [special_characters, numbers]
optional_statics = [verbs, adjectives, colors]

# Themes
superheros = ["Iron Man", "Batman", "Hulk"]
games = ["Minecraft", "GTA", "R6"]
randomness = []
movies = []
tv_shows = []
cities = []
countries = []
animals = []

# Difficulty levels (structure: [module_count, min_len, max_len, min_schar, min_num])
difficulty_one = [3, 8, 10, 0, 0]
difficulty_two = [4, 10, 14, 1, 2]
difficulty_three = [5, 16, 32, 1, 2]

# Ask for difficulty
difficulty_level = int(input("What is your desired difficulty on a scale of 1–3? \n"))
if difficulty_level not in [1, 2, 3]:
    print("Please stay within the parameters.")

# Set difficulty settings
match difficulty_level:
    case 1:
        difficulty_settings = difficulty_one
    case 2:
        difficulty_settings = difficulty_two
    case 3:
        difficulty_settings = difficulty_three

# Theme selection
theme_choice = int(input("Select a theme: Superheros = 1 | Games = 2 | TV Shows = 3 | Movies = 4 | Cities = 5 | Countries = 6 | Animals = 7 | Randomness = 8 \n"))

match theme_choice:
    case 1:
        theme = superheros
    case 2:
        theme = games
    case 3:
        theme = tv_shows
    case 4:
        theme = movies
    case 5:
        theme = cities
    case 6:
        theme = countries
    case 7:
        theme = animals
    case 8:
        theme = randomness

# Module containers (now NOT double-nested)
module_one = []
module_two = []
module_three = []
module_four = []
module_five = []

modules = [module_one, module_two, module_three, module_four, module_five]

# Just structuring your password as a clean string later


# Length-specific filtered city lists (example)
cities_3 = [city for city in cities if len(city) == 3]
cities_4 = [city for city in cities if len(city) == 4]
cities_5 = [city for city in cities if len(city) == 5]
cities_6 = [city for city in cities if len(city) == 6]

# Random indexes for future logic

ran_theme = random.randint(1, 3)
ran_theme_spot = random.randint(0, 3)
ran_static = random.randint(0, len(statics) - 1)
ran_static_opt = random.randint(0, len(statics[ran_static]) - 1)
ran_mod = random.randint(0, 2)
ran_static = random.randint(0, len(statics) - 1)




print("Theme inserted at module:", ran_theme)


# Example theme placement (needs correction later for general case)
if difficulty_level == 1:
    match ran_theme:
        case 1:
            module_one = theme
            modules.pop(0)
        case 2:
            module_two = theme
            modules.pop(1)
        case 3:
            module_three = theme
            modules.pop(2)
    
    

    match ran_mod:
        case 1:
            module_one = [statics[ran_static][ran_static_opt]]
            modules.pop(0)
        case 2:
            module_two = [statics[ran_static][ran_static_opt]]
            modules.pop(1)
        case 3:
            module_three = [statics[ran_static][ran_static_opt]]
            modules.pop(2)
            
    ran_static_opt = random.randint(0, len(statics[ran_static]) - 1)

    match ran_mod:
        case 1:
            module_one = [statics[ran_static][ran_static_opt]]
            modules.pop(0)
        case 2:
            module_two = [statics[ran_static][ran_static_opt]]
            modules.pop(1)
        case 3:
            module_three = [statics[ran_static][ran_static_opt]]
            modules.pop(2)

    
password = module_one + module_two + module_three + module_four + module_five

# Debug print
print("Generated password list:", password)

