prioritySub = 0
for line in open("./day 3/input.txt", 'r'):
    priority = 0
    firstHalf = line[0:len(line)//2]
    secondHalf = line[len(line)//2:]
    common = list(set(firstHalf) & set(secondHalf))
    if common != []:
        if ord(common[0])-38 > 26 and ord(common[0])-38 < 53:
            priority = ord(common[0])-38
        else:
            priority = ord(common[0])-96
        prioritySub = prioritySub + priority
print(prioritySub)
