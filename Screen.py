from enum import Enum

class ScreenType(Enum):
    DEVICE_HOME = 0
    RESULT = 10
    UNKNOWN = 99

class Screen:

    def __init__(self, screenType, matchLocation):
        self.screenType = screenType
        self.matchLocation = matchLocation

    def __str__(self):
        return str(self.screenType)
