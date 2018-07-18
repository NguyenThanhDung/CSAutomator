import cv2
from Screen import Screen
from Screen import ScreenType

class ScreenManager:

    templateFolder = "ScreenTemplate"

    def __init__(self):
        self.threadHold = 1000
        self.templates = {}
        self.templates[ScreenType.DEVICE_HOME] = cv2.imread(ScreenManager.templateFolder + "\DeviceHome.png", 0)
        self.templates[ScreenType.TAP_TO_START] = cv2.imread(ScreenManager.templateFolder + "\TapToStart.png", 0)
        self.templates[ScreenType.RESULT] = cv2.imread(ScreenManager.templateFolder + "\Result.png", 0)

    def GetScreen(self, screenShot):
        screenType = ScreenType.UNKNOWN
        matchLocation = None
        for type in self.templates.keys():
            result = self.MatchTemplate(screenShot.image, self.templates[type])
            if result["IsMatch"] == True:
                screenType = type
                matchLocation = result["Location"]
                break
        return Screen(screenType, matchLocation)

    def MatchTemplate(self, image, template):
        res = cv2.matchTemplate(image, template, cv2.TM_SQDIFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print("[ScreenManager] IsMatch: " + str(min_val) + " -> " + str(min_val < self.threadHold))
        if min_val < self.threadHold:
            return {"IsMatch": True, "Location" : min_loc}
        else:
            return {"IsMatch": False}