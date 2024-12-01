with open("input.txt", "r") as f:
    l = list()
    r = list()

    while True:
        line = f.readline()
        if not line:
            break
        nums = line.split()
        l.append(nums[0])
        r.append(nums[1])
    
    l.sort()
    r.sort()

    total = 0
    for i in range(len(l)):
        dist = int(l[i]) - int(r[i])
        if dist < 0:
            total -= dist
        else:
            total += dist
    print(total)