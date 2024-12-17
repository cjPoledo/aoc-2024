def transform(num):
    if num == 0:
        return 1
    elif len(str(num)) % 2 == 0:
        length = len(str(num))
        return [int(str(num)[: length // 2]), int(str(num)[length // 2 :])]
    else:
        return num * 2024


with open("input.txt", "r") as f:
    map = [int(x) for x in f.readline().strip().split()]

    iterations = 25

    for i in range(iterations):
        new_map = []
        for num in map:
            new_num = transform(num)
            if type(new_num) == list:
                new_map += new_num
            else:
                new_map.append(new_num)
        map = new_map

    print(len(map))
