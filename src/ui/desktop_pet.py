from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QWidget


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

        # Scale while keeping aspect ratio
        pixmap = pixmap.scaled(
            220,
            220,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.label.setPixmap(pixmap)
        self.label.adjustSize()

        self.resize(self.label.size())

        screen = self.screen().availableGeometry() if self.screen() else None
        if screen:
            x = screen.width() - self.width() - 40
            y = screen.height() - self.height() - 40
            self.move(x, y)

        self.drag_position = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = (
                event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            )

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.move(
                event.globalPosition().toPoint() - self.drag_position
            )