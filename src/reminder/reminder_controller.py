from PySide6.QtCore import QObject, QTimer

from src.widgets.reminder_widget import ReminderWidget

from src.config.settings import Settings


class ReminderController(QObject):

    def __init__(self, pet):
        super().__init__()

        self.pet = pet

        self.widget = ReminderWidget()
        self.settings = Settings()

        self.pet.settings_window.settings_changed.connect(
            self.update_interval
        )
        self.pet.reminder_widget = self.widget

        self.pet.bubble_callback = self.position_bubble

        self.widget.hide()

        self.widget.drank_water.connect(self.on_drank)
        self.widget.snoozed.connect(self.on_snooze)

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)   # IMPORTANT

        

        self.timer.timeout.connect(self.start_reminder)

        # Show the first reminder immediately
        QTimer.singleShot(500, self.start_reminder)

    def start_reminder(self):

        if self.widget.isVisible():
            return

        self.pet.play_animation()

        # Show speech bubble after 7 seconds
        QTimer.singleShot(7000, self.show_bubble)

    def show_bubble(self):

        self.position_bubble()

        self.widget.show()

        self.widget.raise_()

    def update_interval(self, minutes):

        # Restart the timer immediately with the new interval
        self.timer.stop()

        self.timer.start(minutes * 60 * 1000)

    def on_drank(self):

        self.widget.hide()

        self.pet.stop_animation()

        self.timer.stop()

        self.timer.start(
            self.get_normal_interval()
        )

    def on_snooze(self):

        self.widget.hide()

        self.pet.stop_animation()

        self.timer.stop()

        self.timer.start(
            self.get_snooze_interval()
        )

    def get_normal_interval(self):

        minutes = self.settings.get_interval()

        return minutes * 60 * 1000


    def get_snooze_interval(self):

        return 10 * 60 * 1000
    
    def position_bubble(self):

        self.widget.adjustSize()

        x = self.pet.x() - self.widget.width() - 10

        y = self.pet.y() + 25

        self.widget.move(x, y)



    