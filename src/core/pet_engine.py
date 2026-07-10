from src.animation.animator import SpriteAnimator
from src.animation.frame_loader import load_frames
from src.animation.animations import AnimationName


class PetEngine:

    def __init__(self, pet):

        self.pet = pet

        self.animator = SpriteAnimator()

        self.animator.set_callback(
            self.pet.set_frame
        )

        self.load_assets()

    def load_assets(self):

        # Temporary: use the existing image until
        # we create the sprite sheet.

        frame = load_frames("assets/sprites/idle")

        if not frame:
            from PySide6.QtGui import QPixmap

            frame = [QPixmap("assets/sprites/character.png")]

        self.animator.add_animation(
            AnimationName.IDLE,
            frame
        )

        self.animator.play(
            AnimationName.IDLE
        )