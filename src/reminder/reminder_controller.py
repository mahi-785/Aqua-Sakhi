from PySide6.QtCore import QObject, QTimer

from src.widgets.reminder_widget import ReminderWidget


class ReminderController(QObject):

    def __init__(self, pet):
        super().__init__()

        self.pet = pet

        self.widget = ReminderWidget()
        self.widget.hide()

        self.widget.drank_water.connect(self.on_drank)
        self.widget.snoozed.connect(self.on_snooze)

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)   # IMPORTANT

        # Development: 30 seconds
        self.normal_interval = 30000
        self.snooze_interval = 10000

        self.timer.timeout.connect(self.start_reminder)

        self.timer.start(self.normal_interval)

    def start_reminder(self):

        # Stop timer while reminder is active
        self.timer.stop()

        self.pet.play_animation()

        # Show speech bubble after 7 seconds
        QTimer.singleShot(7000, self.show_bubble)

    def show_bubble(self):

        self.widget.adjustSize()

        x = self.pet.x() - self.widget.width() - 20
        y = self.pet.y() + 20

        self.widget.move(x, y)

        self.widget.show()
        self.widget.raise_()

    def on_drank(self):

        self.widget.hide()

        self.pet.stop_animation()

        # Start a NEW reminder cycle
        self.timer.start(self.normal_interval)

    def on_snooze(self):

        self.widget.hide()

        self.pet.stop_animation()

        # Snooze
        self.timer.start(self.snooze_interval)