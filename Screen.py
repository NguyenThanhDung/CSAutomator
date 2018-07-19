from enum import Enum

class ScreenType(Enum):
    DEVICE_HOME = 0
    TAP_TO_START = 1
    EVENT_INFO = 2
    DAILY_LOGIN_REWARD = 3
    GAME_HOME = 4
    MAP = 5
    MYSTERIOUS_SANCTUARY = 6
    SHRINE_OF_LIGHT = 7
    GUARDIAN_PLACEMENT = 8
    ACTION_PHASE = 9
    PVE_RESULT_VICTORY = 10
    RESULT = 20
    UNKNOWN = 99

class Screen:

    def __init__(self, screenType, matchLocation):
        self.screenType = screenType
        self.matchLocation = matchLocation

    def ShowName(self):
        print("[Screen] " + str(self.screenType))
