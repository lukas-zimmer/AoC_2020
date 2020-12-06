class Group(object):
    member = 0

    def __init__(self, answers=""):
        self.answer_dict = {}
        self.fill_answer_dict(answers.rsplit("\n"))

    # GET ADD SET
    def add_member(self):
        self.member += 1

    def get_answers(self):
        return self.answer_dict

    # METHODS
    def fill_answer_dict(self, answers):
        for i in answers:
            self.add_member()
            for j in i:
                if j in self.answer_dict:
                    temp = self.answer_dict[j] + 1
                    self.answer_dict.update({j: temp})
                else:
                    self.answer_dict[j] = 1

    def say_yes_to_yourself(self):
        return len(self.answer_dict)

    def say_yes_to_the_world(self):
        counter = 0
        for i in self.answer_dict:
            if self.answer_dict[i] == self.member:
                counter += 1
        return counter

