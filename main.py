import sys

from PySide6.QtWidgets import QApplication

from src.ui.desktop_pet import DesktopPet
from src.reminder.reminder_controller import ReminderController


def main():
    app = QApplication(sys.argv)

    pet = DesktopPet()

    reminder = ReminderController(pet)

    pet.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()