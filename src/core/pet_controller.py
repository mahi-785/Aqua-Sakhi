from src.core.pet_state import PetState


class PetController:
    def __init__(self, pet):
        self.pet = pet
        self.state = PetState.HIDDEN

    def walk_in(self):
        self.state = PetState.WALKING_IN
        self.pet.walk_in()

    def walk_out(self):
        self.state = PetState.WALKING_OUT
        self.pet.walk_out()

    def set_idle(self):
        self.state = PetState.IDLE

    def set_talking(self):
        self.state = PetState.TALKING