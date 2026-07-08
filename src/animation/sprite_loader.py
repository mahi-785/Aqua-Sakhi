from PySide6.QtGui import QPixmap


def load_sprite_sheet(path, frame_width, frame_height):
    sheet = QPixmap(path)

    frames = []

    cols = sheet.width() // frame_width

    for col in range(cols):
        frame = sheet.copy(
            col * frame_width,
            0,
            frame_width,
            frame_height,
        )
        frames.append(frame)

    return frames