enclosed = 0
for line in open("./day 4/input.txt"):
    intervals = line.split(",")
    minmaxSets = []
    for interval in intervals:
        values = []
        minmax = interval.replace("\n", "").split("-")
        i = int(minmax[0])
        while i < int(minmax[1])+1:
            values.append(i)
            i = i+1
        minmaxSets.append(values)
    if len(set(minmaxSets[0]) & set(minmaxSets[1])) > 0:
        enclosed = enclosed+1
print(enclosed)
