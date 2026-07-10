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

        # Development: 30 seconds
        self.timer.setInterval(30000)

        self.timer.timeout.connect(self.start_reminder)

        self.timer.start()

    def start_reminder(self):

        # Play the animation
        self.pet.play_animation()

        # Show reminder after 8 seconds
        QTimer.singleShot(8000, self.show_bubble)

    def show_bubble(self):

        x = self.pet.x() - self.widget.width() - 20
        y = self.pet.y() + 20

        self.widget.move(x, y)

        self.widget.show()

    def on_drank(self):

        self.widget.hide()

        self.pet.stop_animation()

        self.timer.start(30000)

    def on_snooze(self):

        self.widget.hide()

        self.pet.stop_animation()

        self.timer.start(10000)