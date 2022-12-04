prioritySub = 0
lines = open("./day 3/input.txt").readlines()
chunks = [lines[x:x+3] for x in range(0, len(lines), 3)]
for chunk in chunks:
    common = list(set(chunk[0].replace("\n", "")) & set(
        chunk[1].replace("\n", "")) & set(chunk[2].replace("\n", "")))
    if ord(common[0])-38 > 26 and ord(common[0])-38 < 53:
        priority = ord(common[0])-38
    else:
        priority = ord(common[0])-96
    prioritySub = prioritySub + priority
print(prioritySub)
