from PySide6.QtCore import QObject, QTimer, Signal


class ReminderScheduler(QObject):
    reminder_due = Signal()

    def __init__(self):
        super().__init__()

        self.timer = QTimer()

        # 30 seconds while developing
        self.timer.setInterval(30_000)

        self.timer.timeout.connect(self.reminder_due)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def snooze(self):
        self.timer.start(10_000)