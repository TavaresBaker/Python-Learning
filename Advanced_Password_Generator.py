import random
difficulty_to_crack = int(input("On a scale of 1-5, 5 being the most secure, 1 being the least, how secure do you want your password? \n"))
theme = int(input("Select a theme: \n Superheros = 1 | Games = 2 | TV Shows = 3 | Movies = 4 | Cities = 5 | Countries = 6 | Animals = 8 | Randomness = 9 \n"))
section_one = []
section_two = []
section_three = []
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
                                                                                                                        
numbers = list(range(10, 100))

special_characters = [
"!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
"-", "_", "+", "=", "{", "}", "[", "]", "|",
":", ";", "'", "<", ">", ",", ".", "?", "/",
"`", "~"
]            
                                                                                                                        
colors = [
"Red", "Blue", "Green", "Black", "White", "Gray", "Yellow", "Purple", "Orange", "Pink",
"Cyan", "Magenta", "Teal", "Maroon", "Navy", "Olive", "Lime", "Coral", "Beige", "Brown",
"Silver", "Gold", "Turquoise", "Lavender", "Indigo", "Crimson", "Amber", "Violet", "Mint", "Charcoal"                                                                                                                        
]

verbs = [
"Run", "Hack", "Crash", "Load", "Scan", "Block", "Bypass", "Encrypt", "Decrypt", "Ping",
"Boot", "Patch", "Debug", "Deploy", "Monitor", "Exploit", "Secure", "Log", "Authenticate", "Reset",
"Update", "Connect", "Download", "Upload", "Execute", "Filter", "Trace", "Analyze", "Throttle", "Redirect",
"Inject", "Throttle", "Isolate", "Trace", "Backup", "Restore", "Scan", "Compile", "Crash", "Trace",
"Ping", "Hook", "Reset", "Trace", "Scan", "Bind", "Serve", "Configure", "Scan", "Audit"
]
                                                                                                         
adjectives = [
"Sleek", "Rusty", "Bulky", "Shiny", "Matte", "Cracked", "Glossy", "Grimy", "Jagged", "Vibrant",
"Massive", "Tiny", "Moderate", "Sparse", "Ample", "Overwhelming", "Petite", "Hefty", "Abundant", "Meager",
"Snappy", "Sluggish", "Responsive", "Glitchy", "Efficient", "Laggy", "Streamlined", "Overloaded", "Real-time", "Clunky",
"Reliable", "Fragile", "Robust", "Flaky", "Solid", "Corrupted", "Stable", "Sketchy", "Pristine", "Worn",
"Chill", "Intense", "Mysterious", "Ominous", "Cozy", "Grim", "Energetic", "Bleak", "Gritty", "Moody",
"Sarcastic", "Witty", "Laid-back", "Aggressive", "Loyal", "Calculated", "Bold", "Quiet", "Hot-headed", "Cool-headed"
]

match theme:
  case 1:
    theme = [
      [superheros],
      [numbers],
      [special_characters],
    ]
  case 2:
    theme = [
      [games]
      [numbers]
      [special_characters]
    ]

ran_one = random.randint(0, 2)
ran_two = random.randint(0, 2)
ran_three = random.randint(0, 2)
mas_ran = random.randint(0, 100)

# Randomizes the first section of the password

if section_one == [] and mas_ran <= 32:
    section_one = theme.pop(0)
    
elif section_one == [] and 33 <= mas_ran <= 65:
    section_one = theme.pop(1)
    
elif section_one == [] and mas_ran >= 66:
    section_one = theme.pop(2)

# Randomizes the second section of the password

if section_two == [] and mas_ran <= 50:
    section_two = theme.pop(0)
    
elif section_two == [] and mas_ran >= 50:
    section_two = theme.pop(1)

# Applies the leftover value to the third section

section_three = theme.pop(0)
    
 






print(f"Your password is {section_one[0][ran_one]}{section_two[0][ran_two]}{section_three[0][ran_three]}")




                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        





                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        





                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        





                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        





                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        





                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        





                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        





                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        





                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        





                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        





                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        





                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        








