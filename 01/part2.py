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
    

    total = 0
    for n in l:
        c = r.count(n)
        total += int(n) * c
    print(total)