with open("input.txt", "r") as f:
    map = f.readlines()
    map = [x.strip() for x in map]
    max_y = len(map)
    max_x = len(map[0])

    antennas = {}
    for y in range(max_y):
        for x in range(max_x):
            if map[y][x] != ".":
                if map[y][x] not in antennas:
                    antennas[map[y][x]] = [(y, x)]
                else:
                    antennas[map[y][x]].append((y, x))
    antinodes = set()
    for antenna in antennas:
        locs = antennas[antenna]
        for i in range(len(locs)):
            for j in range(i + 1, len(locs)):
                y1, x1 = locs[i]
                y2, x2 = locs[j]
                d_x = x2 - x1
                d_y = y2 - y1

                ax_1 = x1 - d_x
                ay_1 = y1 - d_y
                if (
                    not ax_1 < 0
                    and not ay_1 < 0
                    and not ax_1 >= max_x
                    and not ay_1 >= max_y
                ):
                    antinodes.add((ay_1, ax_1))

                ax_2 = x2 + d_x
                ay_2 = y2 + d_y
                if (
                    not ax_2 < 0
                    and not ay_2 < 0
                    and not ax_2 >= max_x
                    and not ay_2 >= max_y
                ):
                    antinodes.add((ay_2, ax_2))
    print(len(antinodes))
