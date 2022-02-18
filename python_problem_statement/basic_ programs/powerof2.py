num = int(input("Enter the number:"))

for power in range(pow(2, num)):
    print("2 *", power, " = ", (2 * power))
    if ((2 * power) % 400 == 0) or (((2 * power) % 4 == 0) and ((2 * power) % 100 != 0)):
        print("%d is a Leap Year" % (2 * power))
    else:
        print("%d is Not a Leap Year" % (2 * power))