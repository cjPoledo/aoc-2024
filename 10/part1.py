def get_paths(coord, map):
    paths = []
    x, y = coord
    val = int(map[y][x])
    if val == 9:
        return paths, 1

    if y - 1 >= 0 and int(map[y - 1][x]) - val == 1:
        paths.append((x, y - 1))
    if x - 1 >= 0 and int(map[y][x - 1]) - val == 1:
        paths.append((x - 1, y))
    try:
        target = int(map[y + 1][x])
        if target - val == 1:
            paths.append((x, y + 1))
    except:
        pass
    try:
        target = int(map[y][x + 1])
        if target - val == 1:
            paths.append((x + 1, y))
    except:
        pass

    return paths, 0


with open("input.txt", "r") as f:
    map = f.readlines()
    map = [x.strip() for x in map]

    max_x = len(map[0])
    max_y = len(map)

    total = 0

    for y in range(max_y):
        for x in range(max_x):
            if map[y][x] == "0":
                path = [(x, y)]
                passed = []
                while path:
                    passed.append(path.pop())
                    paths, score = get_paths(passed[-1], map)
                    path += [x for x in paths if x not in passed]
                    total += score
    print(total)
