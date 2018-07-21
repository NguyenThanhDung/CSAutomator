import os
import cv2
from enum import Enum

class ScreenType(Enum):
    DEVICE_HOME = 0
    TAP_TO_START = 1
    EVENT_INFO = 2
    DAILY_LOGIN_REWARD = 3
    GAME_HOME = 4
    MAP = 5
    ACTION_PHASE_PLAY_ENABLED = 6
    ACTION_PHASE_PLAY_DISABLED = 7
    
    MYSTERIOUS_SANCTUARY = 10
    SHRINE_OF_LIGHT = 11
    GUARDIAN_PLACEMENT = 12
    PVE_RESULT_VICTORY = 13
    NOT_ENOUGH_SHOES = 14

    BATTLE_LIST_RIVAL_AVAILABLE = 20
    RIVAL_LIST_AVAILABLE = 21
    RIVAL_MATCH_END = 22
    RESULT = 30
    
    UNKNOWN = 99


class Screen:

    def __init__(self, screenType, image):
        self.screenType = screenType
        self.image = image

    def ShowName(self):
        print("[Screen] " + str(self.screenType))

    def Find(self, fileName, precision = 1000):
        filePath = os.path.abspath("ScreenTemplate\\" + fileName)
        targetImage = cv2.imread(filePath, 0)
        res = cv2.matchTemplate(self.image, targetImage, cv2.TM_SQDIFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if min_val < precision:
            return min_loc
        else:
            return None
