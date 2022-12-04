points = 0
for line in open("./day 2/input.txt", 'r'):
    choices = line.replace("\n", "").split(" ")
    accrue = 0
    if choices[1].startswith("X"):
        # lose
        if choices[0].startswith("A"):
            accrue = accrue+3
        elif choices[0].startswith("B"):
            accrue = accrue+1
        else:
            accrue = accrue+2

    if choices[1].startswith("Y"):
        # draw
        accrue = accrue+3
        if choices[0].startswith("A"):
            accrue = accrue+1
        elif choices[0].startswith("B"):
            accrue = accrue+2
        else:
            accrue = accrue+3
    if choices[1].startswith("Z"):
        # win
        accrue = accrue+6
        if choices[0].startswith("A"):
            accrue = accrue+2
        elif choices[0].startswith("B"):
            accrue = accrue+3
        else:
            accrue = accrue+1
    points = points + accrue
print(points)
