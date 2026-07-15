import json
import os


class Settings:

    FILE = "settings.json"

    DEFAULT = {
        "interval": 30,
        "sound": True,
    }

    def __init__(self):

        if not os.path.exists(self.FILE):

            self.save(self.DEFAULT)

    def load(self):

        try:

            with open(self.FILE, "r") as file:

                return json.load(file)

        except Exception:

            return self.DEFAULT.copy()

    def save(self, data):

        with open(self.FILE, "w") as file:

            json.dump(data, file, indent=4)

    def get_interval(self):

        return self.load()["interval"]

    def set_interval(self, minutes):

        data = self.load()

        data["interval"] = minutes

        self.save(data)

    def get_sound(self):

        return self.load()["sound"]

    def set_sound(self, enabled):

        data = self.load()

        data["sound"] = enabled

        self.save(data)