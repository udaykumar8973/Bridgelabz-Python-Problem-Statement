print("Function to find N-th Harmonic Number")


def nthHarmonic(N):
    # H1 = 1
    harmonic = 1.00

    for i in range(2, N + 1):
        harmonic += 1 / i

    return harmonic

if __name__ == "__main__":

    N = int(input("Enter the Number:"))  
    if N != 0:
        print("The Nth harmonic of '", N, "' is '", round(nthHarmonic(N), 2), "'.")
    else:
        print("Enter the Number other than '0'")
