"""CONFIGURABLE FIZZBUZZ.

Prints numbers from 1 to N, substituting multiples of two custom divisors with 'Fizz', 'Buzz', or 'FizzBuzz' if both.
"""

def configurable_fizzbuzz(n, div1, div2):
    for i in range(1, n + 1):
        if i % div1 == 0 and i % div2 == 0:
            print("FizzBuzz")
        elif i % div1 == 0:
            print("Fizz")
        elif i % div2 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    print("***** Configurable FizzBuzz *****")
    try:
        limit = int(input("Enter the maximum number: "))
        divisor_1 = int(input("Enter the first divisor (for Fizz): "))
        divisor_2 = int(input("Enter the second divisor (for Buzz): "))

        if divisor_1 == 0 or divisor_2 == 0:
            print("Error! Divisors cannot be zero!")
        elif limit < 1:
            print("Error! Please enter a maximum number of 1 or greater.")
        else:
            configurable_fizzbuzz(limit, divisor_1, divisor_2)

    except ValueError:
        print("Error! Please enter valid whole numbers only!")