import os


class Config:
    WRITE_HANDLE = os.getenv(
        "WRITE_HANDLE", "/tmp/brightness"
    )  # "/sys/class/backlight/rpi_backlight/brightness"
    READ_HANDLE = os.getenv(
        "READ_HANDLE", "/tmp/actual_brightness"
    )  # "/sys/class/backlight/rpi_backlight/actual_brightness"
    DEBUG = os.getenv("DEBUG", False)
    BROKER = os.getenv("BROKER", "worker0.local")
    TOPIC_NAME = os.getenv("TOPIC_NAME", "screen")
