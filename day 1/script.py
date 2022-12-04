data = []
for line in open("./day 1/input.txt", 'r'):
    try:
        data.append(int(line.replace("\n", "")))
    except:
        data.append(" ")
stringData = ",".join(map(str, data))
data = []
for set in stringData.split(" "):
    total = 0
    setSplit = set.split(",")
    while ("" in setSplit):
        setSplit.remove("")
    for ele in range(0, len(setSplit)):
        total = total + int(setSplit[ele])
    data.append(total)
data.sort()
data = data[::-1]
data = data[0:3]
tot = 0
for ele in range(0, len(data)):
    tot = tot + data[ele]
print(tot)
