val = True

while val:
    c = input('Enter Number more than 10: ')
    b = int(c)
    if b > 10:
        print("Entered number", b, "is more than 10")
        val = False
        print("EXITING")
    else:
        print('Entered Number is: ', b, "is not more than 10, try once more")

