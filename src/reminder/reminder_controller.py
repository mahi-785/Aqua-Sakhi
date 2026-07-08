from PySide6.QtCore import QObject, QTimer

from src.widgets.reminder_widget import ReminderWidget


class ReminderController(QObject):

    def __init__(self, pet):
        super().__init__()

        self.pet = pet

        self.widget = ReminderWidget()

        self.widget.drank_water.connect(self.on_drank)

        self.widget.snoozed.connect(self.on_snooze)

        self.timer = QTimer()

        # Development mode: 30 seconds
        self.timer.setInterval(30000)

        self.timer.timeout.connect(self.show_reminder)

        self.timer.start()

    def show_reminder(self):

        self.pet.walk_in()

        # Wait until pet has walked in
        QTimer.singleShot(1900, self.show_bubble)

    def show_bubble(self):

        x = self.pet.x() - self.widget.width() - 20
        y = self.pet.y() + 20

        self.widget.move(x, y)

        self.widget.show()

    def on_drank(self):

        self.widget.hide()

        self.pet.walk_out()

        # restart normal timer
        self.timer.start(30000)

    def on_snooze(self):

        self.widget.hide()

        self.pet.walk_out()

        # remind again in 10 sec while developing
        self.timer.start(10000)