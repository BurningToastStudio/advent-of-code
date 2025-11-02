reports = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        report = line.split()
        report = [int(lvl) for lvl in report]
        reports.append(report)

safe_reports = 0
for report in reports:
    prev = None
    incressing = None
    is_safe = True
    for level in report:
        if prev is None:
            prev = level
            continue

        diff = level - prev

        if diff == 0:
            is_safe = False
            break

        if abs(diff) > 3:
            is_safe = False
            break

        if incressing is None:
            if prev < level: incressing = True
            elif prev > level: incressing = False
        else:
            if incressing:
                if prev > level:
                    is_safe = False
                    break
            else:
                if prev < level:
                    is_safe = False
                    break

        prev = level

    if is_safe:
        safe_reports += 1

print(safe_reports)