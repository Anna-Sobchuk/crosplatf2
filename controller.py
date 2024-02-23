# controller.py
class PersonController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_user_input(self, first_name, last_name):
        self.model.set_first_name(first_name)
        self.model.set_last_name(last_name)

    def display_full_name(self):
        full_name = self.model.get_full_name()
        self.view.display_full_name(full_name)

    def set_view(self, view):
        self.view = view
