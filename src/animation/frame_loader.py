from pathlib import Path

from PySide6.QtGui import QPixmap


def load_frames(folder):

    folder = Path(folder)

    frames = []

    if not folder.exists():
        return frames

    for file in sorted(folder.iterdir()):

        if file.suffix.lower() == ".png":
            frames.append(QPixmap(str(file)))

    return frames
