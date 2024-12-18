with open("input.txt", "r") as f:
    map = [list(x.strip()) for x in f.readlines()]
    max_y = len(map)
    max_x = len(map[0])
    solution = 0

    global_visited = set()

    def get_borders(y, x, region, get_dirs=False):
        top = y - 1
        bottom = y + 1
        left = x - 1
        right = x + 1
        coords = set()
        dirs = set()

        if top >= 0 and map[top][x] == region:
            coords.add((top, x))
        else:
            dirs.add("top")
        if left >= 0 and map[y][left] == region:
            coords.add((y, left))
        else:
            dirs.add("left")
        if bottom < max_y and map[bottom][x] == region:
            coords.add((bottom, x))
        else:
            dirs.add("bottom")
        if right < max_x and map[y][right] == region:
            coords.add((y, right))
        else:
            dirs.add("right")

        if get_dirs:
            return dirs

        return coords

    def get_sides(regions):
        sorted_regions_y = sorted(regions)
        sorted_regions_x = sorted(regions, key=lambda x: (x[1], x[0]))
        sides = 0
        curr_coord = None
        last_other_coord = None
        connected_top = False
        connected_bot = False
        for coord in sorted_regions_y:
            if curr_coord != coord[0]:
                connected_top = False
                connected_bot = False
                curr_coord = coord[0]
            elif not last_other_coord is None:
                if abs(last_other_coord - coord[1]) != 1:
                    connected_top = False
                    connected_bot = False
            last_other_coord = coord[1]
            dirs = get_borders(
                coord[0], coord[1], map[coord[0]][coord[1]], get_dirs=True
            )
            if not connected_top and "top" in dirs:
                sides += 1
                connected_top = True
            elif not "top" in dirs:
                connected_top = False
            if not connected_bot and "bottom" in dirs:
                sides += 1
                connected_bot = True
            elif not "bottom" in dirs:
                connected_bot = False
        curr_coord = None
        connected_top = False
        connected_bot = False
        for coord in sorted_regions_x:
            if curr_coord != coord[1]:
                connected_top = False
                connected_bot = False
                curr_coord = coord[1]
            elif not last_other_coord is None:
                if abs(last_other_coord - coord[0]) != 1:
                    connected_top = False
                    connected_bot = False
            last_other_coord = coord[0]
            dirs = get_borders(
                coord[0], coord[1], map[coord[0]][coord[1]], get_dirs=True
            )
            if not connected_top and "left" in dirs:
                sides += 1
                connected_top = True
            elif not "left" in dirs:
                connected_top = False
            if not connected_bot and "right" in dirs:
                sides += 1
                connected_bot = True
            elif not "right" in dirs:
                connected_bot = False
        return sides

    for y in range(max_y):
        for x in range(max_x):
            if (y, x) in global_visited:
                continue

            region = map[y][x]

            to_visit = set([(y, x)])
            visited = set()

            sides = 0
            area = 0

            while to_visit:
                curr_coords = to_visit.pop()
                coords_to_visit = get_borders(curr_coords[0], curr_coords[1], region)
                area += 1
                visited.add(curr_coords)
                to_visit.update(coords_to_visit - visited)
            sides = get_sides(visited)
            solution += area * sides
            global_visited.update(visited)

    print(solution)
