from PySide6.QtCore import Qt, Signal, QPropertyAnimation
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGraphicsDropShadowEffect,
)


class ReminderWidget(QWidget):

    drank_water = Signal()
    snoozed = Signal()

    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setOffset(0, 6)
        shadow.setColor(QColor(0, 0, 0, 70))
        self.setGraphicsEffect(shadow)

        self.setStyleSheet("""

        QWidget{
            background:#FDFEFF;
            border:2px solid #BFE8FF;
            border-radius:24px;
        }

        QLabel{
            border:none;
            background:transparent;
            font-size:16px;
            color:#355C7D;
            font-weight:600;
        }

        QPushButton{

            background:#77C9FF;

            color:white;

            border:none;

            border-radius:16px;

            padding:10px;

            font-size:14px;

            font-weight:bold;

            min-width:130px;

        }

        QPushButton:hover{

            background:#58B8F7;

        }

        QPushButton:pressed{

            background:#3DAAEF;

        }

        """)

        self.message = QLabel("💧 Time to drink some water!")

        self.drink_button = QPushButton("💙 I Drank")

        self.snooze_button = QPushButton("😴 Snooze")

        self.drink_button.clicked.connect(self.drank_water.emit)

        self.snooze_button.clicked.connect(self.snoozed.emit)

        layout = QVBoxLayout()

        layout.setContentsMargins(22, 18, 22, 18)

        layout.setSpacing(16)

        layout.addWidget(self.message)

        row = QHBoxLayout()

        row.setSpacing(12)

        row.addWidget(self.drink_button)

        row.addWidget(self.snooze_button)

        layout.addLayout(row)

        self.setLayout(layout)

        self.adjustSize()

        self.fade = QPropertyAnimation(self, b"windowOpacity")

        self.fade.setDuration(350)

    def showEvent(self, event):

        self.setWindowOpacity(0)

        self.fade.stop()

        self.fade.setStartValue(0)

        self.fade.setEndValue(1)

        self.fade.start()

        super().showEvent(event)