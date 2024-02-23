# main.py
import tkinter as tk
from model import PersonModel
from gui_view import PersonGUIView
from console_view import PersonConsoleView
from controller import PersonController

def main():
    print("Choose the mode:")
    print("1. GUI mode (Tkinter)")
    print("2. Console mode (CLI)")

    choice = input("Enter your choice (1 or 2): ")

    model = PersonModel()

    if choice == "1":
        root = tk.Tk()
        controller = PersonController(model, None)
        view = PersonGUIView(root, controller)  # Змінено тут: передаємо контролер як аргумент
        controller.set_view(view)
        view.run()
    elif choice == "2":
        view = PersonConsoleView()
        controller = PersonController(model, view)
        controller.set_user_input(view.get_user_input("Enter First Name: "), view.get_user_input("Enter Last Name: "))
        controller.display_full_name()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
