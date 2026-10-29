def median(values):
    s = sorted(values)
    if not s:
        raise ValueError("median requires at least one value")

    middle = len(s) // 2
    if len(s) % 2 == 0:
        return (s[middle - 1] + s[middle]) / 2
    return s[middle]
