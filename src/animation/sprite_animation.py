from PySide6.QtCore import QObject, QTimer
from PySide6.QtGui import QPixmap


class SpriteAnimation(QObject):
    def __init__(self, frames, fps=10):
        super().__init__()

        self.frames = frames
        self.index = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.next_frame)
        self.timer.start(int(1000 / fps))

        self.callback = None

    def next_frame(self):
        if not self.frames:
            return

        self.index = (self.index + 1) % len(self.frames)

        if self.callback:
            self.callback(self.current_frame())

    def current_frame(self):
        return self.frames[self.index]

    def set_callback(self, callback):
        self.callback = callback