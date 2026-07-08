from PySide6.QtCore import QObject, QTimer

from src.widgets.reminder_widget import ReminderWidget


class ReminderController(QObject):

    def __init__(self, pet):
        super().__init__()

        self.pet = pet

        self.widget = ReminderWidget()

        self.widget.drank_water.connect(self.drank)
        self.widget.snoozed.connect(self.snooze)

        self.timer = QTimer()

        # 30 seconds for testing
        self.timer.start(30000)

        self.timer.timeout.connect(self.show_reminder)

    def show_reminder(self):

        self.pet.walk_in()

        self.widget.move(
            self.pet.x() - 220,
            self.pet.y()
        )

        self.widget.show()

    def drank(self):

        self.widget.hide()

        self.pet.walk_out()

    def snooze(self):

        self.widget.hide()

        self.pet.walk_out()

        self.timer.start(10000)