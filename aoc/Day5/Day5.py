from aoc.Day5.Seat import Seat


class DayFive(object):
    def __init__(self):
        self.seats = [Seat(i) for i in open("inputs/Day5")]
        self.seat_id_list = self.__sorted_seat_list()

    def get_highest_seat_id(self):
        return max(self.seat_id_list)

    def where_is_my_seat(self):
        # https://www.w3schools.com/python/ref_set_difference.asp
        return int(set(range(self.seat_id_list[0], self.seat_id_list[-1])).difference(self.seat_id_list).pop())

    def __sorted_seat_list(self):
        return sorted([i.seat_id for i in self.seats])

    def __str__(self):
        return "Highest Seat ID: " + str(self.get_highest_seat_id()) + "\n" + "My Seat: " + str(self.where_is_my_fucking_seat())
