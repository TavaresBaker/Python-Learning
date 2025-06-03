# Last semester's gradebook

last_semester_gradebook = [
    ["Politics", 80],
    ["Latin", 96],
    ["Dance", 97],
    ["Architecture", 65]
]

# Current semester subjects and grades

subjects = ["Physics", "Calculus", "Poetry", "History"]
grades = [98, 97, 85, 88]

# Building the gradebook

gradebook = [
    ["Physics", 98],
    ["Calculus", 97],
    ["Poetry", 85],
    ["History", 88]
]

# Add new subjects

gradebook.append(["Computer Science", 100])
gradebook.append(["Visual Arts", 93])

# Update Visual Arts grade to 98

gradebook[-1][-1] = 98

# Replace Poetry grade with "Pass"

gradebook[2].remove(85)
gradebook[2].append("Pass")

# Print updated gradebook

print("Current Semester Gradebook:")
print(gradebook)

# Combine last semester with current semester gradebook

full_gradebook = last_semester_gradebook + gradebook

# Print full gradebook

print("\nFull Gradebook (Every Semester):")
print(full_gradebook)
