from PySide6.QtCore import QObject, QTimer


class Animation(QObject):
    def __init__(self, frames=None, fps=8):
        super().__init__()

        self.frames = frames or []
        self.current = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.next_frame)

        self.callback = None

        self.set_fps(fps)

    def set_frames(self, frames):
        self.frames = frames
        self.current = 0

        if self.callback and self.frames:
            self.callback(self.frames[0])

    def set_callback(self, callback):
        self.callback = callback

    def start(self):
        if self.frames:
            self.timer.start()

    def stop(self):
        self.timer.stop()

    def set_fps(self, fps):
        self.timer.setInterval(int(1000 / fps))

    def next_frame(self):

        if not self.frames:
            return

        self.current += 1

        if self.current >= len(self.frames):
            self.current = 0

        if self.callback:
            self.callback(self.frames[self.current])
            