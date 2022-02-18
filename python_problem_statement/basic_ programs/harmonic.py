print("Function to find N-th Harmonic Number")

def nthHarmonic(num):
    harmonic = 1.00  # initially harmonic is one

    for number in range(2, num + 1):
        harmonic += 1 / number

    return harmonic

if __name__ == "__main__":

    num = int(input("Enter the Number:"))
    if num != 0:
        print("The Nth harmonic of '", num, "' is '", round(nthHarmonic(num), 2), "'.")
    else:
        print("Enter the Number other than '0'")