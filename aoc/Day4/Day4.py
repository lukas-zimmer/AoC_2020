from aoc.Day4.Passport import Passport


class DayFour:
    DEBUG = True

    def __init__(self):
        self.passport_list = []
        self.__fill_passport_list()

    def __fill_passport_list(self):
        with open('inputs/day4', 'r') as f:
            temp_passport_list = f.read().split("\n\n")

        for i in range(len(temp_passport_list)):
            temp_passport_list[i] = temp_passport_list[i].replace("\n", " ").split(" ")

        for p in temp_passport_list:
            dust = dict(i.split(":") for i in p)
            self.passport_list.append(Passport(dust))

    def count_valid_passports(self):
        counter_pone = 0
        counter_ptwo = 0
        for i in self.passport_list:
            if i.is_valid():
                counter_pone += 1
            if i.is_totally_valid():
                counter_ptwo += 1
        return "Part One: " + str(counter_pone), "Part Two: " + str(counter_ptwo)
