import random 

special_characters = []
numbers = []
verbs = []
adjectives = []
colors = []


superheros = [
"Iron Man",
"Batman",
"Hulk"
]

games = [
"Minecraft",
"GTA",
"R6"
]

randomness = [
]

movies = [
]

tv_shows = [
]

cities = [
]

countries = [
]

animals = [
]

difficulty_one = [
# The first number is the module count. The second is the minimum length. The third is the maximum length. Fourth is the minimum number of special characters. Fifth is the minimum number of numbers.
    3,
    8,
    10,
    0,
    0
]

difficulty_two = [
    4,
    10,
    14,
    1,
    2
]

difficulty_three = [
    5,
    16,
    32,
    1,
    2,
]

desired_difficulty = int(input("What is your desired difficulty on a scale of 1-3? "))
if desired_difficulty not in [1, 2, 3]:
    print("Please stay within the paramaters")
match desired_difficulty:
    case 1:
        desired_difficulty = difficulty_one
    case 2:
        desired_difficulty = difficulty_two
    case 3:
        desired_difficulty = difficulty_three




#COME BACK AND VERIFY THE DIFFERENT THEMES HERE WITH THEIR COORESPONDING NUMBERS sweetheart!
theme = int(input("Select a theme: \n Superheros = 1 | Games = 2 | TV Shows = 3 | Movies = 4 | Cities = 5 | Countries = 6 | Animals = 7 | Randomness = 8 \n"))
match theme:
  case 1:
    theme = [
      [superheros],
    ]
  case 2:
    theme = [
      [games] 
    ]
  case 3:
    theme = [
      [tv_shows],
    ]
  case 4:
    theme = [
      [movies]
    ]
  case 5:
    theme = [
      [cities],
    ]
  case 6:
    theme = [
      [countries]
    ]
  case 7:
    theme = [
      [animals],
    ]
  case 8:
    theme = [
      [randomness]
    ]  

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
module_one = []
module_two = []
module_three = []
module_four = []
module_five = []

modules = [
    [module_one],
    [module_two],
    [module_three],
    [module_four],
    [module_five]
]

password = module_one + module_two + module_three + module_four + module_five





cities_3 = [city for city in cities if len(city) == 3]
cities_4 = [city for city in cities if len(city) == 4]
cities_5 = [city for city in cities if len(city) == 5]
citiec_6 = [city for city in cities if len(city) == 6]






ran_schar = random.randint()
ran_num
ran_verb
ran_adj
ran_color
ran_theme
ran_theme_spot = random.randint(1, 3)





if desired_difficulty == 1:
    match ran_theme:
        case 1:
            module_one = theme
        case 2:
            module_two = theme
        case 3:
            module_three = theme

































print(password)
