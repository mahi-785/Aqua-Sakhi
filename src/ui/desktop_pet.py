from PySide6.QtCore import Qt, QPoint, QPropertyAnimation
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QWidget


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

        pixmap = QPixmap("assets/sprites/character.png")

        if pixmap.isNull():
            raise FileNotFoundError(
                "Couldn't load assets/sprites/character.png"
            )

        pixmap = pixmap.scaled(
            220,
            220,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.label.setPixmap(pixmap)
        self.label.adjustSize()

        self.resize(self.label.size())

        screen = QApplication.primaryScreen().availableGeometry()

        self.final_x = screen.width() - self.width() - 40
        self.final_y = screen.height() - self.height() - 40

        # Start off-screen to the left
        self.move(-self.width(), self.final_y)

        self.drag_position = QPoint()

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

    def walk_in(self):
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(1800)
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(
            QPoint(self.final_x, self.final_y)
        )
        self.animation.start()

    def walk_out(self):
        screen = QApplication.primaryScreen().availableGeometry()

        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(1800)
        self.animation.setStartValue(self.pos())
        self.animation.setEndValue(
            QPoint(screen.width() + self.width(), self.final_y)
        )
        self.animation.start()