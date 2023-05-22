ls = [555, 66, 112, 12, 1, 0, -8]

n = 0
for i in ls:
    if i > 50:
        print(n, '-', i)
        n = n + 1

for i in {1, "asdf", 3, 4}:
    print('Next FOR:', i)

for k in range(200, 250):
    print(k**2)

for k in ls:
    print(k**3)
