from aoc.Day3.Day3 import DayThree
import os


def main():
    filepath = os.path.join("inputs", "day3")
    print(filepath)
    a = DayThree()
    p1 = a.count_trees()
    print(p1)

    b = DayThree()
    p2 = b.count_trees(1, 1)
    p2 *= b.count_trees()
    p2 *= b.count_trees(5, 1)
    p2 *= b.count_trees(7, 1)
    p2 *= b.count_trees(1, 2)
    print(p2)


if __name__ == '__main__':
    main()
