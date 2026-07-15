from PySide6.QtCore import Qt, QPoint, QSize
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QWidget, QLabel, QApplication


class DesktopPet(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.label = QLabel(self)
        self.label.setStyleSheet("background: transparent;")

        self.movie = QMovie("assets/videos/water_reminder.gif")

        

        self.movie.setScaledSize(QSize(220, 220))

        self.movie.setCacheMode(QMovie.CacheAll)

        self.movie.setSpeed(100)

        if not self.movie.isValid():
            raise FileNotFoundError(
                "Could not load assets/videos/water_reminder.gif"
            )

        # Scale the GIF while keeping aspect ratio.
        # Increase these values if you want AquaSakhi larger.
        self.movie.setScaledSize(self.movie.scaledSize())

        self.label.setMovie(self.movie)

        self.movie.frameChanged.connect(self._frame_changed)

        self.drag_position = QPoint()

        self.resize(320, 320)

        self.label.resize(self.size())

        self.move_to_bottom_right()

        self.hide()

    def play_animation(self):
        """Show AquaSakhi and play the GIF from the beginning."""

        self.show()

        self.raise_()

        self.movie.stop()

        self.movie.start()


    def stop_animation(self):
        """Hide AquaSakhi after the reminder."""

        self.movie.stop()

        self.hide()


    def _frame_changed(self, frame):

        if frame == self.movie.frameCount() - 1:

            self.movie.setPaused(True)

        pixmap = self.movie.currentPixmap()

        if pixmap.isNull():
            return

        scaled = pixmap.scaled(
            500,
            260,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )

        self.label.setPixmap(scaled)

        self.label.resize(scaled.size())

        self.resize(scaled.size())


    def mousePressEvent(self, event):

        if event.button() == Qt.MouseButton.LeftButton:

            self.drag_position = (
                event.globalPosition().toPoint()
                - self.frameGeometry().topLeft()
            )


    def mouseMoveEvent(self, event):

        if event.buttons() & Qt.MouseButton.LeftButton:

            self.move(
                event.globalPosition().toPoint()
                - self.drag_position
            )


    def move_to_bottom_right(self):

        screen = QApplication.primaryScreen().availableGeometry()

        x = screen.width() - self.width() - 40

        y = screen.height() - self.height() - 40

        self.move(x, y)


    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.label.resize(self.size())


    def closeEvent(self, event):

        self.movie.stop()

        super().closeEvent(event)