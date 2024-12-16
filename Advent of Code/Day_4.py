from collections import defaultdict as dd







with open('Day_4.txt', 'r') as file:
    data = file.readlines()


a = dd(set)


for x, row in enumerate(data):
    for y, col in enumerate(row):
        a[col].add((x, y))

counter = 0
#print(a)
#print(type(a))

for x, y in a["X"]:
    for ax, ay in [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
        for i, char in enumerate("XMAS"):
            if (x + (ax * i), y + (ay * i)) not in a[char]:
                break

        else:
            counter += 1

counter_2 = 0

for x, y in a["A"]:
    if (x - 1, y - 1) in a["M"]:
        if (x + 1, y - 1) in a["M"] and (x - 1, y + 1) in a["S"] and (x + 1, y + 1) in a["S"]:
            counter_2 += 1
        elif (x - 1, y + 1) in a["M"] and (x + 1, y - 1) in a["S"] and (x + 1, y + 1) in a["S"]:
            counter_2 += 1

    elif (x + 1, y + 1) in a["M"]:
        if (x + 1, y - 1) in a["M"] and (x - 1, y + 1) in a["S"] and (x - 1, y - 1) in a["S"]:
            counter_2 += 1
        elif (x - 1, y + 1) in a["M"] and (x + 1, y - 1) in a["S"] and (x - 1, y - 1) in a["S"]:
            counter_2 += 1

print(counter)

print(counter_2)






