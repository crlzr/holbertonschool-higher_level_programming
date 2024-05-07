#!/usr/bin/python3

# multiples of 3 = Fizz
# multiples of 5 = Buzz
# multiples of 3 and 5 = FizzBuzz

def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end ="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
