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
            Qt.FramelessWindowHint
            | Qt.Tool
            | Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setStyleSheet("""
            QWidget{
                background:white;
                border-radius:20px;
                border:2px solid #A7D8F5;
            }

            QLabel{
                font-size:16px;
                color:#333333;
            }

            QPushButton{
                background:#6EC6FF;
                color:white;
                border:none;
                border-radius:10px;
                padding:8px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#42A5F5;
            }
        """)

        self.message = QLabel("💧 Time to drink some water!")

        self.drink_button = QPushButton("💙 I Drank Water")
        self.snooze_button = QPushButton("😴 Snooze")

        self.drink_button.clicked.connect(self.drank_water.emit)
        self.snooze_button.clicked.connect(self.snoozed.emit)

        layout = QVBoxLayout(self)
        layout.addWidget(self.message)

        row = QHBoxLayout()
        row.addWidget(self.drink_button)
        row.addWidget(self.snooze_button)

        layout.addLayout(row)

        self.adjustSize()