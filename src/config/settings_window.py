from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QRadioButton,
    QButtonGroup,
    QSpinBox,
    QCheckBox,
)

from src.config.settings import Settings


class SettingsWindow(QWidget):

    settings_changed = Signal(int)

    def __init__(self):
        super().__init__()

        self.settings = Settings()


        self.setWindowTitle("🌸 AquaSakhi Settings")

        self.setFixedSize(360, 370)

        self.setStyleSheet("""

        QWidget{
            background:#FDFEFF;
            font-size:14px;
        }

        QLabel{
            color:#355C7D;
            font-size:16px;
            font-weight:bold;
        }

        QPushButton{
            background:#77C9FF;
            color:white;
            border:none;
            border-radius:12px;
            padding:10px;
            font-weight:bold;
        }

        QPushButton:hover{
            background:#58B8F7;
        }

        """)

        title = QLabel("💧 Reminder Interval")

        self.group = QButtonGroup(self)

        self.r30 = QRadioButton("Every 30 minutes")
        self.r60 = QRadioButton("Every 1 hour")
        self.r120 = QRadioButton("Every 2 hours")
        self.rCustom = QRadioButton("Custom")

        self.group.addButton(self.r30)
        self.group.addButton(self.r60)
        self.group.addButton(self.r120)
        self.group.addButton(self.rCustom)

        self.custom_minutes = QSpinBox()
        self.custom_minutes.setRange(5, 720)
        self.custom_minutes.setSuffix(" min")

        self.sound = QCheckBox("🔊 Enable sounds")

        self.save_button = QPushButton("Save Settings")

        layout = QVBoxLayout(self)

        layout.setContentsMargins(25,25,25,25)

        layout.setSpacing(14)

        layout.addWidget(title)

        layout.addWidget(self.r30)
        layout.addWidget(self.r60)
        layout.addWidget(self.r120)

        row = QHBoxLayout()

        row.addWidget(self.rCustom)
        row.addWidget(self.custom_minutes)

        layout.addLayout(row)

        layout.addSpacing(10)

        layout.addWidget(self.sound)

        layout.addStretch()

        layout.addWidget(self.save_button)

        self.load_settings()

        self.save_button.clicked.connect(self.save_settings)

    def load_settings(self):

        interval = self.settings.get_interval()

        if interval == 30:
            self.r30.setChecked(True)

        elif interval == 60:
            self.r60.setChecked(True)

        elif interval == 120:
            self.r120.setChecked(True)

        else:
            self.rCustom.setChecked(True)
            self.custom_minutes.setValue(interval)

        self.sound.setChecked(
            self.settings.get_sound()
        )

    def save_settings(self):

        if self.r30.isChecked():
            interval = 30

        elif self.r60.isChecked():
            interval = 60

        elif self.r120.isChecked():
            interval = 120

        else:
            interval = self.custom_minutes.value()

        self.settings.set_interval(interval)

        self.settings.set_sound(
            self.sound.isChecked()
        )

        self.settings_changed.emit(interval)

        self.close()