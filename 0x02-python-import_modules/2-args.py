#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv)-1 == 0):
        print(f"0 arguments.")
    else:
        print(f"{len(sys.argv)-1} argument:")
        for i in range(len(sys.argv)-1):
            print(f"{i+1}: {sys.argv[i+1]}")
