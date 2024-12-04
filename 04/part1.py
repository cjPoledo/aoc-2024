with open("input.txt", "r") as f:
    ws = f.readlines()
    ws = [l.strip() for l in ws]
    x_max = len(ws[0])
    y_max = len(ws)
    count = 0
    dirs = (
        (0, -1),  # n
        (1, -1),  # ne
        (1, 0),  # e
        (1, 1),  # se
        (0, 1),  # s
        (-1, 1),  # sw
        (-1, 0),  # w
        (-1, -1),  # nw
    )

    for y in range(y_max):
        for x in range(x_max):
            if ws[y][x] == "X":
                for dir in dirs:
                    try:
                        coords = list()
                        for i in range(4):
                            tx = x + i * dir[0]
                            ty = y + i * dir[1]
                            if tx < 0 or ty < 0:
                                raise Exception("err")
                            coords.append((tx, ty))

                        if (
                            "".join([ws[coord[1]][coord[0]] for coord in coords])
                            == "XMAS"
                        ):
                            count += 1
                    except:
                        continue
    print(count)
