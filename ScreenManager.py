import cv2
from Screen import Screen
from Screen import ScreenType

class ScreenManager:

    templateFolder = "ScreenTemplate"
    defaultPrecisionThreadhold = 1000

    def __init__(self):
        self.templates = {}
        self.templates[ScreenType.DEVICE_HOME] = [cv2.imread(ScreenManager.templateFolder + "\DeviceHome.png", 0)]
        self.templates[ScreenType.TAP_TO_START] = [cv2.imread(ScreenManager.templateFolder + "\TapToStart.png", 0)]
        self.templates[ScreenType.EVENT_INFO] = [cv2.imread(ScreenManager.templateFolder + "\EventInfo.png", 0)]
        self.templates[ScreenType.DAILY_LOGIN_REWARD] = [cv2.imread(ScreenManager.templateFolder + "\DailyLoginReward.png", 0), 6000]
        self.templates[ScreenType.GAME_HOME] = [cv2.imread(ScreenManager.templateFolder + "\GameHome.png", 0)]
        self.templates[ScreenType.RESULT] = [cv2.imread(ScreenManager.templateFolder + "\Result.png", 0)]

    def GetScreen(self, screenShot):
        screenType = ScreenType.UNKNOWN
        matchLocation = None
        for type in self.templates.keys():
            if len(self.templates[type]) > 1:
                result = self.MatchTemplate(type, screenShot.image, self.templates[type][0], self.templates[type][1])
            else:
                result = self.MatchTemplate(type, screenShot.image, self.templates[type][0], ScreenManager.defaultPrecisionThreadhold)
            if result["IsMatch"] == True:
                screenType = type
                matchLocation = result["Location"]
                break
        return Screen(screenType, matchLocation)

    def MatchTemplate(self, screenType, image, template, precisionThreadhold):
        res = cv2.matchTemplate(image, template, cv2.TM_SQDIFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print("[ScreenManager] IsMatch(" + str(screenType) + "): " + str(min_val) + " -> " + str(min_val < precisionThreadhold))
        if min_val < precisionThreadhold:
            return {"IsMatch": True, "Location" : min_loc}
        else:
            return {"IsMatch": False}