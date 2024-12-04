with open("input.txt", "r") as f:
    ws = f.readlines()
    ws = [l.strip() for l in ws]
    x_max = len(ws[0])
    y_max = len(ws)
    count = 0

    for y in range(y_max):
        for x in range(x_max):
            if ws[y][x] == "A":
                try:
                    if y - 1 < 0 or x - 1 < 0:
                        raise Exception("err")

                    if (
                        (ws[y - 1][x - 1] == "M" and ws[y + 1][x + 1] == "S")
                        or (ws[y - 1][x - 1] == "S" and ws[y + 1][x + 1] == "M")
                    ) and (
                        (ws[y - 1][x + 1] == "M" and ws[y + 1][x - 1] == "S")
                        or (ws[y - 1][x + 1] == "S" and ws[y + 1][x - 1] == "M")
                    ):
                        count += 1
                except:
                    continue
    print(count)
