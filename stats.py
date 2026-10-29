def median(values):
    s = sorted(values)
    if not s:
        return 0
    return s[len(s) // 2]
