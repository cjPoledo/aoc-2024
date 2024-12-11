def extract_eq(eq):
    eq = eq.strip()
    eq = eq.split(":")

    return [int(eq[0])] + [int(n) for n in eq[1].split()]


with open("input.txt", "r") as f:
    eqs = f.readlines()
    eqs = [extract_eq(e) for e in eqs]
    total = 0

    for eq in eqs:
        print(
            "Calculating...", int((eqs.index(eq) + 1) / len(eqs) * 100), "%", end="\r"
        )
        target = eq[0]
        nums = eq[1:]
        ops = 3 ** (len(nums) - 1)
        curr_ops = 0

        while curr_ops < ops:
            ternary_ops = []
            temp_ops = curr_ops
            for _ in range(len(nums) - 1):
                ternary_ops.append(str(temp_ops % 3))
                temp_ops //= 3
            ternary_ops.reverse()
            result = nums[0]

            for i in range(len(ternary_ops)):
                if ternary_ops[i] == "0":
                    result += nums[i + 1]
                elif ternary_ops[i] == "1":
                    result *= nums[i + 1]
                else:
                    result = result * (10 ** len(str(nums[i + 1]))) + nums[i + 1]
                if result > target:
                    break

            if result == target:
                total += target
                break
            else:
                curr_ops += 1

    print()
    print(total)
