#!/usr/bin/python3
def fizzbuzz():
    for y in range(1, 101):
        if (y % 15 == 0):
            print("{}".format("FizzBuzz "), end="")
        elif (y % 5 == 0):
            print("{}".format("Buzz "), end="")
        elif (y % 3 == 0):
            print("{}".format("Fizz "), end="")
        else:
            print("{}".format(y), end=" ")
