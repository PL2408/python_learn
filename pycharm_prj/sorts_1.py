ls = [555, 66, 112, 12, 1, 0, -8]

mi = min(ls[0], ls[1])
ma = max(ls[0], ls[1])
ls[0:2] = [mi, ma]

print(ls)