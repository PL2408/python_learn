print(5.8)
print("echo var's")
print(5, 6, 'green')
print("Result is:", 18)

ls = [4, 5.3, "green", [1, 12]]

# this is comment and is not treated by Python
print("List is -", ls)
print("----------------------------")

print("Class of ls is:", type(ls))

ls.append("New Item")
print("List is -", ls)

ls.append("Petryk")
ls.insert(0, "Vitaliy")
ls[3] = 'Green Vitaliy'

ls[1] = ls[1] + 8

ls[4].insert(16575, [45132])

print("List is -", ls)

print(ls[4])
a = 56
b = [156]
print(a)
print(b)
d = b[0]
c = a + d

print(c)

print("================")

ls = [1, 2, 3, 4, 5, 6, 7, "a", "s", "d", "f", "g", "h"]

print(ls[2], ls[7])
print(ls[3:10])
print(ls[::-1])

ls.pop()

print(len(ls))