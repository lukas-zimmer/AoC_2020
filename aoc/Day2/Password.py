class Password:
    min_rate = 0
    max_rate = 0
    character = ''
    password = ''

    CONST_ONE = 1

    def __init__(self, min_rate, max_rate, char, password):
        self.min_rate = int(min_rate)
        self.max_rate = int(max_rate)
        self.character = char
        self.password = password

    def is_valid_p1(self):
        # .count(value) Return the number (int) of times the value appears in the string:
        return self.min_rate <= self.password.count(self.character) <= self.max_rate

    def is_valid_p2(self):
        return (self.password[self.min_rate - self.CONST_ONE] is self.character) ^ (
                    self.password[self.max_rate - self.CONST_ONE] is self.character)

    def __str__(self):
        return str(self.min_rate) + " " + str(self.max_rate) + " " + self.character + " " + self.password
