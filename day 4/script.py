enclosed = 0
for line in open("./day 4/input.txt"):
    intervals = line.split(",")
    minmaxSets = []
    for interval in intervals:
        values = []
        minmax = interval.replace("\n", "").split("-")
        minmaxSets.append(minmax)
    if (int(minmaxSets[0][0]) <= int(minmaxSets[1][0]) and int(minmaxSets[0][1]) >= int(minmaxSets[1][1])):
        enclosed = enclosed + 1
    elif (int(minmaxSets[0][0]) >= int(minmaxSets[1][0]) and int(minmaxSets[0][1]) <= int(minmaxSets[1][1])):
        enclosed = enclosed + 1
print(enclosed)
