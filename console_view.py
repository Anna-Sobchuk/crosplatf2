# console_view.py
class PersonConsoleView:
    def get_user_input(self, prompt):
        return input(prompt)

    def display_full_name(self, full_name):
        print(f"Full Name: {full_name}")
