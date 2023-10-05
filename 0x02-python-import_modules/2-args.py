#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if len(sys.argv) < 2:
        print("0 arguments.")
    else:
        print(f"{count} arguments:")
        for i in range(1, count):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
