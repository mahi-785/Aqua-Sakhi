import sys

from PySide6.QtWidgets import QApplication

from src.ui.desktop_pet import DesktopPet


def main():
    app = QApplication(sys.argv)

    pet = DesktopPet()
    pet.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()