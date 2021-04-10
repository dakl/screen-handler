from .base import Accessory


class MockAccessory(Accessory):
    def set_state(self, state):
        return 1

    def get_status(self):
        return 0
