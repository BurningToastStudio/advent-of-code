total = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        stack = []

        for i, digit in enumerate(line):
            while stack and len(stack) + (100 - i) > 12 and stack[-1] < digit:
                stack.pop()
            if len(stack) < 12:
                stack.append(digit)

        val = int("".join(stack))
        total += val

print(total)