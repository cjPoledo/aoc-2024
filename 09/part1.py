with open("input.txt", "r") as f:
    map = f.read().strip()
    chksm = 0
    end_i = len(map) - 1
    end_i_file = int(map[end_i])
    curr_i = 0

    for i in range(0, len(map), 2):
        if i == end_i:
            for j in range(end_i_file):
                chksm += int(curr_i * (end_i / 2))
                curr_i += 1
            break

        file = int(map[i])
        free = int(map[i + 1])

        for j in range(file):
            chksm += int(curr_i * (i / 2))
            curr_i += 1

        for j in range(free):
            if end_i_file < 1:
                end_i -= 2
                end_i_file = int(map[end_i])
            chksm += int(curr_i * (end_i / 2))
            end_i_file -= 1
            curr_i += 1

    print(chksm)
