# Create a 3 x 4 array of your favorite hobbies or sports. Use for loop to display values or items you have.

hobbies = [
    ["Drawing", "Reading", "Listening to music", "Playing the guitar"],
    ["Writing", "Sleeping", "Journalling", "Playing games"],
    ["Sightseeing", "Painting", "Watching TV shows", "Going to museums"]
]

for row in hobbies:
    for hobby in row:
        print(f"| {hobby.center(20)} ", end = "")
    print("|")
