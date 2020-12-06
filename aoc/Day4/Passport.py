import re


class Passport(object):

    def __init__(self, dictionary=None):
        if dictionary is None:
            self.dictionary = dict()
        else:
            self.dictionary = dictionary

        self.values = {'byr': lambda s: len(s) == 4 and 1920 <= int(s) <= 2002,
                       'iyr': lambda s: len(s) == 4 and 2010 <= int(s) <= 2020,
                       'eyr': lambda s: len(s) == 4 and 2020 <= int(s) <= 2030,
                       'hgt': lambda s: self.hgt_is_valid(s),
                       'hcl': lambda s: re.match(r'#[a-f0-9]{6}', s),
                       'ecl': lambda s: s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                       'pid': lambda s: len(s) == 9 and s.isdigit()
                       }

    def hgt_is_valid(self, s):
        # https://www.askpython.com/python/string/python-raw-strings
        # https://www.w3schools.com/python/python_regex.asp
        # \d -> starts with a digit ; () --> groups  ;  | --> xor  ;  $ --> ends with
        hgt = re.match(r'^(\d+)(cm|in)$', s)
        # hgt --> [123cm, 123, cm]
        if hgt:
            if hgt[2] == "cm" and 150 <= int(hgt[1]) <= 193:
                return True
            elif hgt[2] == "in" and 59 <= int(hgt[1]) <= 76:
                return True
            else:
                return False
        return False

    def is_valid(self):
        return all(v in self.dictionary for v in self.values)

    def is_totally_valid(self):
        if self.is_valid():
            for i in self.values:
                fn = self.values[i]
                if not fn(self.dictionary[i]):
                    return False
            return True
        return False

    def __str__(self):
        return str(self.dictionary)
