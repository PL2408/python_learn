a = 1099
b = 55

print("a:", a)
print("b:", b)
c = a
a = b
b = c
print('----------------')
print("a:", a)
print("b:", b)
print('----------------')
a, b = b, a
print("a:", a)
print("b:", b)

ls = [3, 4, 6, 8, 9]
ls[0], ls[1], ls[3] = 7, 7, 7
print(ls)

a = 15
b = 17
print(min(a,b))

if a > b:
    print(a)
else:
    print(b)


a, b = -2507569, -6567457
