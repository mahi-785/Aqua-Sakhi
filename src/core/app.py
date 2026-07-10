from PySide6.QtWidgets import QApplication

from src.ui.desktop_pet import DesktopPet
from src.reminder.reminder_controller import ReminderController


class AquaSakhiApp:

    def __init__(self):

        self.app = QApplication.instance() or QApplication([])

        self.pet = DesktopPet()

        self.reminder = ReminderController(self.pet)

    def run(self):

        return self.app.exec()