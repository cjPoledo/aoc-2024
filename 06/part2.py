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
        return True
    return False


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
    init_guard = guard.copy()
    total = 0
    for row in range(len(map)):
        print("Calculating: ", int(row / len(map) * 100), "%")
        for col in range(len(map[row])):
            guard = init_guard.copy()
            test_map = map.copy()
            test_map[row] = test_map[row][:col] + "#" + test_map[row][col + 1 :]
            loop_checker = None
            loop_checker_active = False
            move_history = [guard.copy()]
            while True:
                loop_checker_active = not loop_checker_active
                if loop_checker_active:
                    loop_checker = move_history.pop(0)
                exited = guard_move(guard, test_map)
                move_history.append(guard.copy())
                if loop_checker == guard:
                    total += 1
                    break
                if exited is True:
                    break
    print(total)
