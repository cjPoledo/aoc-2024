def check_ord(update, rules):
    for i in range(1, len(update)):
        for j in range(i):
            if l[j] in rules[l[i]]:
                return (j, i)
    return True


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
        to_add = False
        index = check_ord(l, ord_rul)
        while index is not True:
            to_add = True
            temp = l[index[0]]
            l[index[0]] = l[index[1]]
            l[index[1]] = temp
            index = check_ord(l, ord_rul)
        if to_add:
            total += int(l[int(len(l) / 2)])

    print(total)
