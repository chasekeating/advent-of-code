# Open puzzle input data
with open("data/calories.txt", "r") as f:

    # Read puzzle input "f" and split new line via regex
    data = f.read().split("\n\n")

    # Split string into line item list
    data = [[int(item) for item in inputlist.splitlines()] for inputlist in data]

    # Quick maths
    data = [sum(inputlist) for inputlist in data]

    # Sort list
    data = sorted(data)

# Print Step 1 Result
print("Step 1:", data[-1], "= Top 1 Elf Total Calorie Count")

# Print Step 2 Result
print("Step 1:", sum(data[-3:]), "= Top Three Elves Total Calorie Count")
