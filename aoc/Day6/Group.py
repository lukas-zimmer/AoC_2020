class Group(object):
    member = 0

    def __init__(self, answers=""):
        self.answer_dict = {}
        self.answers = [i for i in answers.rsplit("\n")]
        self.__setup()

    def __setup(self):
        self.__set_answer_dict()
        self.__set_member()

    # GET ADD SET
    def __set_member(self):
        self.member = len(self.answers)

    # METHODS
    def __set_answer_dict(self):
        for i in self.answers:
            for j in i:
                if j in self.answer_dict:
                    temp = self.answer_dict[j] + 1
                    self.answer_dict.update({j: temp})
                else:
                    self.answer_dict[j] = 1

    def say_yes_to_coffee(self):
        return len(self.answer_dict)

    def say_yes_to_tee(self):
        counter = 0
        for i in self.answer_dict:
            if self.answer_dict[i] == self.member:
                counter += 1
        return counter

