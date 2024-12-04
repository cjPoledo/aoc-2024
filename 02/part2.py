with open("input.txt", "r") as f:
    safe = 0
    counter = 0

    while True:
        line = f.readline()
        counter += 1
        if not line:
            break
        line = line.split()
        nums = [int(n) for n in line]

        last = nums[0]
        direction = nums[0] - nums[1]  # +dec, -inc
        unsafe = False

        for i in range(1, len(nums)):
            diff = last - nums[i]
            # check diff
            if abs(diff) < 1 or abs(diff) > 3:
                unsafe = True
                break
            # check same dir
            if diff * direction < 0:
                unsafe = True
                break
            last = nums[i]

        if unsafe:
            for i in range(len(nums)):
                removed_one = [nums[j] for j in range(len(nums)) if j != i]
                last = removed_one[0]
                direction = removed_one[0] - removed_one[1]  # +dec, -inc
                unsafe = False

                for i in range(1, len(removed_one)):
                    diff = last - removed_one[i]
                    # check diff
                    if abs(diff) < 1 or abs(diff) > 3:
                        unsafe = True
                        break
                    # check same dir
                    if diff * direction < 0:
                        unsafe = True
                        break
                    last = removed_one[i]

                if not unsafe:
                    break

        if not unsafe:
            safe += 1

    print(safe)
