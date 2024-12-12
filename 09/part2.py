with open("input.txt", "r") as f:
    map = [int(x) for x in list(f.read().strip())]
    files = [(int(i / 2), map[i]) for i in range(0, len(map), 2)]
    spaces = [map[i] for i in range(1, len(map), 2)]

    new_files = files.copy()

    file_positions = {file: idx for idx, file in enumerate(new_files)}

    for i in range(len(files) - 1, -1, -1):
        print(
            f"Rearranging files... {i:04d} remaining",
            end="\r",
        )
        file = files[i]
        for j in range(len(spaces)):
            if j < file_positions[file] and spaces[j] >= file[1]:
                file_i = file_positions[file]
                new_files.insert(j + 1, new_files.pop(file_i))

                for k in range(j + 1, len(new_files)):
                    file_positions[new_files[k]] = k

                spaces[j] -= file[1]

                new_space = file[1]
                if file_i < len(spaces):
                    new_space += spaces.pop(file_i)
                spaces[file_i - 1] += new_space

                spaces.insert(j, 0)

                break

    chksm = 0
    index = 0
    for i in range(len(new_files)):
        for j in range(new_files[i][1]):
            chksm += new_files[i][0] * index
            index += 1
        for j in range(spaces[i]):
            index += 1
    print()
    print(chksm)
