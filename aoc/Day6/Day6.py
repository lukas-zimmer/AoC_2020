from aoc.Day6.Group import Group


class DaySix:
    def __init__(self):
        self.groups = [Group(i) for i in open("inputs/day6").read().split("\n\n")]

    def part_one(self):
        yes = 0
        for i in self.groups:
            yes += i.say_yes_to_coffee()
        return yes

    def part_two(self):
        yes = 0
        for i in self.groups:
            yes += i.say_yes_to_tee()
        return yes

    def __str__(self):
        return str(self.part_one()) + "\n" + str(self.part_two())
