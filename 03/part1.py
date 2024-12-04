import re

with open("input.txt", "r") as f:
    seq = f.read()
    valid_mul = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", seq)

    total = 0

    for exp in valid_mul:
        nums = exp.split(",")
        total += int(nums[0].strip("mul(")) * int(nums[1].strip(")"))

    print(total)
