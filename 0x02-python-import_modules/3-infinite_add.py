#!/usr/bin/python3

def main():
    import sys
    if sys.argv == 1:
        print("{:d}".format(0))
        return
    sum = 0
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])
        print("{:d}".format(sum))


if __name__ == "__main__":
    main()
