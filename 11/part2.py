def transform(num):
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 0:
        half_length = len(str(num)) // 2
        divisor = 10**half_length
        return [num // divisor, num % divisor]
    else:
        return [num * 2024]


with open("input.txt", "r") as f:
    map = [int(x) for x in f.readline().strip().split()]
    count = {}

    for num in map:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    iterations = 75

    for _ in range(iterations):
        new_count = {}
        for num in count:
            outputs = transform(num)
            for output in outputs:
                if output in new_count:
                    new_count[output] += count[num]
                else:
                    new_count[output] = count[num]
        count = new_count

    print(sum(list(count.values())))
