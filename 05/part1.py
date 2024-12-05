with open("input.txt", "r") as f:
    string = f.readlines()
    sep_index = string.index("\n")
    ord_rul_str = string[:sep_index]
    upd = string[sep_index + 1 :]

    ord_rul_str = [item.strip("\n") for item in ord_rul_str]
    upd = [item.strip("\n").split(",") for item in upd]

    ord_rul = {}
    for rul in ord_rul_str:
        rul = rul.split("|")
        try:
            ord_rul[rul[0]].append(rul[1])
        except:
            ord_rul[rul[0]] = [rul[1]]

    total = 0
    for l in upd:
        bad = False
        for i in range(1, len(l)):
            for j in range(i):
                if l[j] in ord_rul[l[i]]:
                    bad = True
                    break
            if bad:
                break
        if not bad:
            total += int(l[int(len(l) / 2)])
    print(total)
