
class Seat(object):
    row = 0
    column = 0
    seat_id = 0
    CONST_TWO = 2

    def __init__(self, code=""):
        self.setup(code)

    def setup(self, code):
        row_code, column_code = code[:7], code[7:]

        self.__set_row(row_code)
        self.__set_column(column_code)
        self.__set_seat_id()

    # SETTER
    def __set_row(self, row_code):
        self.row = self.__binary_space_partitioning("F", "B", 128, row_code)
        return self.row

    def __set_column(self, column_code):
        self.column = self.__binary_space_partitioning("L", "R", 8, column_code)
        return self.column

    def __set_seat_id(self):
        self.seat_id = (self.row * 8) + self.column
        return

    # GETTER
    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_seat_id(self):
        return self.seat_id

    # METHODS
    def __binary_space_partitioning(self, lower, upper, range_max, code):
        temp_array = [i for i in range(0, range_max)]
        for element in code:
            if element == lower:
                temp_array = temp_array[: int(len(temp_array) / self.CONST_TWO)]
            elif element == upper:
                temp_array = temp_array[int(len(temp_array) / self.CONST_TWO):]

        return temp_array[0]

    def __str__(self):
        return "Row: " + str(self.row) + "\n" + "Column: " + str(self.column) + "\n" + "Seat ID: " + str(self.seat_id)

