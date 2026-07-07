from dataclasses import dataclass


@dataclass
class Settings:
    reminder_interval: int = 60
    snooze_time: int = 10
    volume: float = 0.5
    character_scale: float = 1.0
    animation_speed: float = 1.0


settings = Settings()