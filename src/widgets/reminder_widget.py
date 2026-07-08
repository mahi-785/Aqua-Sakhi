from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class ReminderWidget(QWidget):
    drank_water = Signal()
    snoozed = Signal()

    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.Tool
        )

        self.setStyleSheet("""
            QWidget{
                background:white;
                border-radius:18px;
                border:2px solid #BFE7FF;
            }

            QLabel{
                font-size:15px;
            }

            QPushButton{
                border:none;
                border-radius:10px;
                padding:8px;
                background:#7EC8E3;
                color:white;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#5EB8D8;
            }
        """)

        text = QLabel("💧 Time to drink some water!")

        drank = QPushButton("💙 I Drank Water")
        snooze = QPushButton("😴 Snooze 10 min")

        drank.clicked.connect(self.drank_water.emit)
        snooze.clicked.connect(self.snoozed.emit)

        layout = QVBoxLayout(self)
        layout.addWidget(text)

        buttons = QHBoxLayout()
        buttons.addWidget(drank)
        buttons.addWidget(snooze)

        layout.addLayout(buttons)

        self.adjustSize()