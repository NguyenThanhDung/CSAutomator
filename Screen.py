import os, errno
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
    REWARD_INFO = 8
    
    MYSTERIOUS_SANCTUARY = 10
    SHRINE_OF_LIGHT = 11
    GUARDIAN_PLACEMENT = 12
    PVE_RESULT_VICTORY = 13
    PVE_RESULT_REPEAT_RESULT = 14
    NOT_ENOUGH_SHOES = 15

    BATTLE_LIST = 20
    BATTLE_LIST_REFRESH_CONFIRMATION = 21
    BATTLE_LIST_REFRESH_WITH_MOONSTONE = 22
    RIVAL_LIST = 23
    RIVAL_MATCH_END = 25
    BATTLE_RESULT_WIN = 26
    BATTLE_RESULT_LOSE = 27
    NOT_ENOUGH_TICKETS = 28
    BATTLE_REFRESH_RESET = 29
    BATTLE_NEW_SEASON = 30
    BATTLE_RANKING = 31
    BATTLE_DEFENSE_RECORD = 32

    DAILY_MISSION = 40
    DAILY_MISSION_POPUP = 41

    MAIL_BOX_INBOX_TAB = 45
    MAIL_BOX_COLLECT = 46

    SHOP = 50
    SHOP_DIALOG_IS_OPENNING = 51
    SHOP_DIALOG_PURCHASE_CONFIRMATION = 52

    SUMMON = 60
    SUMMON_BASIC_DONE = 61
    SUMMON_MYSTEROUS_DONE = 62
    
    DIALOG_WEEKLY_LIMITED = 80
    DIALOG_LIMITED_OFFER = 81
    DIALOG_SUGGESTED_ITEM = 82
    DIALOG_SHOES_RECHARGE_FP = 83
    DIALOG_SHOES_RECHARGE_II = 84
    DIALOG_NOT_ENOUGH_FP = 85
    DIALOG_PURCHASE_COMPLETE = 86
    DIALOG_UNSTABLE_NETWORK = 87

    LEVEL_UP = 90
    
    UNKNOWN = 99


class Screen:

    def __init__(self, screenType, image):
        self.screenType = screenType
        self.image = image

    def ShowName(self):
        self.Log(str(self.screenType))

    def Find(self, fileName, precision = 10000):
        filePath = os.path.abspath("ScreenTemplate\\" + fileName)
        targetImage = cv2.imread(filePath, 0)
        if targetImage is None:
            return None
        res = cv2.matchTemplate(self.image, targetImage, cv2.TM_SQDIFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        self.Log(fileName.ljust(50) + " " + str(min_val).rjust(15))
        if min_val < precision:
            return min_loc
        else:
            return None

    def Save(self):
        dirPath = os.path.abspath( "Temp/")
        try:
            os.makedirs(dirPath)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        
        filePath = os.path.join(dirPath, str(self.screenType) + ".png")
        cv2.imwrite(filePath, self.image)

        return filePath

    def Log(self, log):
        print("[Screen] " + log)
        return None