with open("input.txt", "r") as f:
    map = [list(x.strip()) for x in f.readlines()]
    max_y = len(map)
    max_x = len(map[0])
    solution = 0

    global_visited = set()

    def get_borders(y, x, region):
        top = y - 1
        bottom = y + 1
        left = x - 1
        right = x + 1
        borders = 0
        coords = set()

        if top >= 0 and map[top][x] == region:
            coords.add((top, x))
        else:
            borders += 1
        if left >= 0 and map[y][left] == region:
            coords.add((y, left))
        else:
            borders += 1
        if bottom < max_y and map[bottom][x] == region:
            coords.add((bottom, x))
        else:
            borders += 1
        if right < max_x and map[y][right] == region:
            coords.add((y, right))
        else:
            borders += 1

        return borders, coords

    for y in range(max_y):
        for x in range(max_x):
            if (y, x) in global_visited:
                continue

            region = map[y][x]

            to_visit = set([(y, x)])
            visited = set()

            perimeter = 0
            area = 0

            while to_visit:
                curr_coords = to_visit.pop()
                reg_perimeter, coords_to_visit = get_borders(
                    curr_coords[0], curr_coords[1], region
                )
                perimeter += reg_perimeter
                area += 1
                visited.add(curr_coords)
                to_visit.update(coords_to_visit - visited)
            solution += area * perimeter
            global_visited.update(visited)

    print(solution)
