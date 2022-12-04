points = 0
for line in open("./day 2/input.txt", 'r'):
    choices = line.replace("\n", "").split(" ")
    accrue = 0
    if (choices[0].startswith("A") & choices[1].startswith("Y")) | (choices[0].startswith("B") & choices[1].startswith("Z")) | (choices[0].startswith("C") & choices[1].startswith("X")):
        accrue = accrue + 6
    if (choices[0].startswith("A") & choices[1].startswith("X")) | (choices[0].startswith("B") & choices[1].startswith("Y")) | (choices[0].startswith("C") & choices[1].startswith("Z")):
        accrue = accrue + 3
    # Accrue based on points
    if choices[1].startswith("X"):
        accrue = accrue + 1
    elif choices[1].startswith("Y"):
        accrue = accrue + 2
    else:
        accrue = accrue + 3
    points = points + accrue
print(points)
