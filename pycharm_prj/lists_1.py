# lists
divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona']
print(divchata) # output list
print(len(divchata)) # output length
print(type(divchata)) # output type (list)

drb = list(('Marichka', 'Alyona', 'Kristina', 'Alyona'))  # note the double round-brackets
print(drb) # output list (tuple)

# Access list items
divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona'] #->
print(divchata[1]) # output 'Alyona'
print(divchata[-3]) # output 'Alyona'

divchata.append('Diana') # output add 'Diana' to end of list
print(divchata)

print(divchata[1:4]) # output 'Alyona', 'Kristina', 'Alyona', 'Diana'
print(divchata[:4]) # output 'Diana', 'Alyona', 'Kristina', 'Alyona', 'Marichka',
print(divchata[2:]) # output 'Kristina', 'Alyona', 'Diana'
print("divchata[-1:-2]", divchata[-2:-1]) # output 'Alyona'

# Check if the element exists
# divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona', 'Diana']
if 'Alyona' in divchata:
    print('Alyona is the hottest of all this girls')


# Change the value of an element
# divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona', 'Diana']
divchata[0] = 'miss beach'
print(divchata)
divchata[0:2] = ['miss beach', 'big eyes']
print(divchata)

divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona', 'Diana']
divchata[3:4] = ['Ganya', 'Liza']
print("divchata[3:4] = [Ganya', 'Liza']", divchata)

# Insert
divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona', 'Diana']
divchata.insert(3, 'Liza')
print(divchata)

# Extend
divchata = ['Kristina', 'Diana', 'Ganya']
chotki_divchata = ['Alyona', 'Marichka']
chotki_divchata.extend(divchata)
print(chotki_divchata)

# Other objects
divchata = ['Kristina', 'Diana', 'Ganya']
tuple_divchata = ('Alyona', 'Marichka')
divchata.extend(tuple_divchata)
print(divchata)

# Remove
divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona', 'Diana']
divchata.remove('Kristina')
print(divchata)

# Pop
divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona', 'Diana']
divchata.pop(3)
print("pop", divchata) # output deleted 'Alyona'

divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona', 'Diana']
divchata.pop()
print("pop_1",divchata) # output deleted the last value

# Del
divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona', 'Diana']
del divchata[0]
print("del",divchata) # output deleted 'Marichka'

divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona', 'Diana']
del divchata # output deleted all list

# Clear
divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona', 'Diana']
divchata.clear()
print("clear",divchata) # output deleted all values inside list

# For cycle
divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona', 'Diana']
for x in divchata:
    print(x)  # output all names on column

for x in 'Marichka':
    print(x) # output letters on column

#??????????
divchata = ['Marichka', 'Alyona', 'Kristina', 'Alyona', 'Diana']
for i in range(len(divchata)):
  print(divchata[i])
