from pathlib import Path

from PySide6.QtGui import QPixmap


class AssetManager:
    def __init__(self):
        self.root = Path("assets")

    def load_image(self, relative_path: str) -> QPixmap:
        path = self.root / relative_path

        if not path.exists():
            raise FileNotFoundError(path)

        return QPixmap(str(path))


assets = AssetManager()