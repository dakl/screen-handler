from app import config
import structlog

from .base import Accessory

logger = structlog.getLogger(__name__)

STATE_MAP = {
    "ON": 1,
    "OFF": 0,
}


class Screen(Accessory):
    def __init__(
        self,
        name: str,
        read_handle: str = None,
        write_handle: str = None,
    ):
        self.name = name
        self.read_handle = read_handle or config.READ_HANDLE
        self.write_handle = write_handle or config.WRITE_HANDLE

    def set_state(self, state: int) -> None:
        if state == 0:
            self.set_brightness(0)
        elif state == 1:
            self.set_brightness(255)

    def get_state(self) -> int:
        brightness = self.get_brightness()
        if brightness > 0:
            return 1
        else:
            return 0

    def set_brightness(self, value: int) -> None:
        """ Brightness is expected to come in as an int in the range 0-255."""
        with open(self.write_handle, "w") as f:
            f.write(str(value) + "\n")

    def get_brightness(self) -> int:
        with open(self.read_handle, "r") as f:
            return int(f.read().strip())

    def handle(self, payload):
        if "brightness" in payload:
            b = int(payload.get("brightness"))
            self.set_brightness(b)
        elif "state" in payload:
            if payload.get("state") == "OFF":
                self.set_brightness(0)
            elif payload.get("state") == "ON":
                self.set_brightness(255)
