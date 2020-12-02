def split_it_up(line):
    rate, char, pwd = line.split(" ", 2)
    min_rate, max_rate = rate.split("-", 1)
    # remove colon a: --> a
    char = char[:-1]
    # remove linebreak https://www.w3schools.com/python/ref_string_rstrip.asp
    pwd = pwd.rstrip("\n")

    return int(min_rate), int(max_rate), char, pwd


def is_min_max(min_rate, max_rate, char, pwd):
    # .count(value) Return the number (int) of times the value appears in the string:
    return min_rate <= pwd.count(char) <= max_rate


def is_valid(pos1, pos2, char, pwd):
    # https://appdividend.com/2020/06/10/python-xor-operator-example-bitwise-operator-in-python/
    # https://www.askpython.com/python/string/string-equals-check-in-python
    return (pwd[pos1 - 1] is char) ^ (pwd[pos2 - 1] is char)


def get_data():
    data = open('./inputs/day2', 'r')
    return data


def part_one():

    data = get_data()

    valid_pwd_count = 0

    for line in data:
        min_rate, max_rate, char, pwd = split_it_up(line)

        # .count(value) Return the number (int) of times the value appears in the string:
        if is_min_max(min_rate, max_rate, char, pwd):
            valid_pwd_count += 1

    return valid_pwd_count


def part_two():
    data = get_data()

    valid_pwd_count = 0

    for line in data:
        min_rate, max_rate, char, pwd = split_it_up(line)

        if is_valid(min_rate, max_rate, char, pwd):
            valid_pwd_count += 1

    return valid_pwd_count


class DayTwo:
    part_one = part_one()
    part_two = part_two()
