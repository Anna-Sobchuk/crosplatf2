class PersonModel:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
