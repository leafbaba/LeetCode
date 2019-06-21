people = 13
count = 0
while 1:
    if people >= 26:
        break
    people = people * (1 + 0.008)
    count = count + 1
print("%d 年后，我国人口可达到26亿" % count)