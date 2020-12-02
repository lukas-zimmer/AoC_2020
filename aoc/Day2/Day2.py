from aoc.Day2.Password import Password


def split_it_up(line):
    rate, char, pwd = line.split(" ", 2)
    min_rate, max_rate = rate.split("-", 1)
    # remove colon a: --> a
    char = char[:-1]
    # remove linebreak https://www.w3schools.com/python/ref_string_rstrip.asp
    pwd = pwd.rstrip("\n")

    return int(min_rate), int(max_rate), char, pwd


class DayTwo:
    def __init__(self):
        self.password_list = []
        self.fill_password_list()

    def fill_password_list(self):
        data = open('./inputs/day2', 'r')

        for line in data:
            min_rate, max_rate, char, pwd = split_it_up(line)
            self.password_list.append(Password(min_rate, max_rate, char, pwd))

    def print_list(self):
        print(self.password_list)

    def part_one(self):
        counter = 0
        for i in self.password_list:
            if i.is_valid_p1():
                counter += 1
        return counter

    def part_two(self):
        counter = 0
        for i in self.password_list:
            if i.is_valid_p2():
                counter += 1
        return counter
