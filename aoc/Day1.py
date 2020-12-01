from utils.logger import Logger


class DayOnePartOne:
    log = Logger.logger

    def __init__(self):
        self.papyrus = [int(i) for i in open('./inputs/day1', 'r')]

    def part_one(self):
        self.log.info('START - Day 1 Part 1')
        for x in self.papyrus:
            for y in self.papyrus:
                if x + y == 2020:
                    self.log.info('x: %(x)s , y: %(y)s' % {'x': str(x), 'y': str(y)})
                    self.log.info('x*y: ' + str(x * y))
                    self.log.info('STOP')
                    return x * y

    def part_two(self):
        self.log.info('START - Day 1 Part 2')
        for x in self.papyrus:
            for y in self.papyrus:
                for z in self.papyrus:
                    if x + y + z == 2020:
                        self.log.info('x: %(x)s , y: %(y)s , %(z)s' % {'x': str(x), 'y': str(y), 'z': str(z)})
                        self.log.info('x*y*z: ' + str(x * y * z))
                        self.log.info('STOP')
                        return x * y * z
