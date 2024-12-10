def guard_move(guard, map):
    try:
        if guard[2] == "^":
            if guard[0] - 1 < 0:
                raise Exception
            if map[guard[0] - 1][guard[1]] == "#":
                guard[2] = ">"
            else:
                guard[0] -= 1
        elif guard[2] == ">":
            if map[guard[0]][guard[1] + 1] == "#":
                guard[2] = "v"
            else:
                guard[1] += 1
        elif guard[2] == "v":
            if map[guard[0] + 1][guard[1]] == "#":
                guard[2] = "<"
            else:
                guard[0] += 1
        elif guard[2] == "<":
            if guard[1] - 1 < 0:
                raise Exception
            if map[guard[0]][guard[1] - 1] == "#":
                guard[2] = "^"
            else:
                guard[1] -= 1
    except:
        return guard, True
    return guard, False


with open("input.txt", "r") as f:
    map = f.readlines()
    guard = list()
    guard_directions = ["^", ">", "v", "<"]
    for row in range(len(map)):
        map[row] = map[row].strip()
        if len(guard) == 0:
            for dir in guard_directions:
                if dir in map[row]:
                    guard = [row, map[row].index(dir), dir]
                    break
    while True:
        map[guard[0]] = map[guard[0]][: guard[1]] + "X" + map[guard[0]][guard[1] + 1 :]
        guard, exited = guard_move(guard, map)
        if exited is True:
            print("".join(map).count("X"))
            break
        else:
            map[guard[0]] = (
                map[guard[0]][: guard[1]] + "X" + map[guard[0]][guard[1] + 1 :]
            )
