class DayThree:

    __CONST_TREE = '#'

    def __init__(self):
        self.forest = [str(i.rstrip("\n")) for i in open('inputs/day3', 'r')]

    def count_trees(self, steps_right=3, steps_down=1):
        length, height = len(self.forest[0]), len(self.forest)
        current_pos = 0
        tree_counter = 0

        for i in range(0, height, steps_down):
            tree_counter += int(self.forest[i][current_pos] == self.__CONST_TREE)
            current_pos = (current_pos + steps_right) % length

        return tree_counter
