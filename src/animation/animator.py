from PySide6.QtCore import QObject

from src.animation.animation import Animation
from src.animation.animations import AnimationName


class SpriteAnimator(QObject):

    def __init__(self):
        super().__init__()

        self.animation = Animation()

        self.animations = {}

    def add_animation(self, name, frames):

        self.animations[name] = frames

    def play(self, name):

        if name not in self.animations:
            return

        self.animation.stop()

        self.animation.set_frames(
            self.animations[name]
        )

        self.animation.start()

    def set_callback(self, callback):

        self.animation.set_callback(callback)