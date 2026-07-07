from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QSoundEffect


class SoundManager:
    def __init__(self):
        self.effects = {}

    def load(self, name: str, filename: str):
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile(str(Path("assets/sounds") / filename)))
        effect.setVolume(0.4)
        self.effects[name] = effect

    def play(self, name: str):
        if name in self.effects:
            self.effects[name].play()


sounds = SoundManager()