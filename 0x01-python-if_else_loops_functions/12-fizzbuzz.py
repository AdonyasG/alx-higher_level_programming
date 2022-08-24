#!/usr/bin/python3
def fizzbuzz():
    a = "FizzBuzz"
    b = a[:4]
    c = a[4:]
    for i in range(1, 101):
        if i % 15 == 0:
            print("{} ".format(a), end='')
        elif i % 3 == 0:
            print("{} ".format(b), end='')
        elif i % 5 == 0:
            print("{} ".format(c), end='')
        else:
            print("{} ".format(i), end='')
