def extract_eq(eq):
    eq = eq.strip()
    eq = eq.split(":")

    return [int(eq[0])] + [int(n) for n in eq[1].split()]


with open("input.txt", "r") as f:
    eqs = f.readlines()
    eqs = [extract_eq(e) for e in eqs]
    total = 0

    for eq in eqs:
        target = eq[0]
        nums = eq[1:]
        ops = 2 ** (len(nums) - 1)
        curr_ops = 0

        while curr_ops < ops:
            binary_ops = bin(curr_ops)[2:].zfill(len(nums) - 1)
            result = nums[0]

            for i in range(len(binary_ops)):
                if binary_ops[i] == "0":
                    result += nums[i + 1]
                else:
                    result *= nums[i + 1]
                if result > target:
                    break

            if result == target:
                total += target
                break
            else:
                curr_ops += 1

    print(total)
