import re

with open("input.txt", "r") as f:
    seq = f.read()
    valid_mul = [e[0] for e in re.findall(r"((mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\)))", seq)]
    total = 0
    do = True

    for exp in valid_mul:
        if exp == "do()":
            do = True
            continue
        if exp == "don't()":
            do = False
            continue

        if do:
            nums = exp.split(",")
            total += int(nums[0].strip("mul(")) * int(nums[1].strip(")"))

    print(total)
