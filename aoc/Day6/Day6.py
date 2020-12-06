from aoc.Day6.Group import Group


class DaySix:
    def __init__(self):
        self.groups = [Group(i) for i in open("inputs/day6").read().split("\n\n")]

    def yes(self):
        yes = 0
        for i in self.groups:
            yes += i.say_yes_to_yourself()
        return yes

    def yesyes(self):
        yes = 0
        for i in self.groups:
            yes += i.say_yes_to_the_world()
        return yes
