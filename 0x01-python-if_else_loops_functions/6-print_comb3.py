#!/usr/bin/python3
for i in range(10):
    for a in range(1+i+(10*i), 10*(i + 1)):
        if a == 89:
            print(f'{a}')
            break
        print("{:02d}, ".format(a), end='')
