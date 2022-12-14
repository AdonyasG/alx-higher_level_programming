#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    i = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if (i == "+"):
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        exit(0)
    elif (i == "-"):
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        exit(0)
    elif (i == "*"):
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        exit(0)
    elif (i == "/"):
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
