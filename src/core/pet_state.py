from enum import Enum, auto


class PetState(Enum):
    HIDDEN = auto()
    WALKING_IN = auto()
    IDLE = auto()
    TALKING = auto()
    WALKING_OUT = auto()
    SNOOZED = auto()