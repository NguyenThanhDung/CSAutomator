import cv2
from Screen import Screen
from Screen import ScreenType

class ScreenManager:

    templateFolder = "ScreenTemplate"

    def __init__(self):
        self.threadHold = 1000
        self.templates = {}
        self.templates[ScreenType.DEVICE_HOME] = cv2.imread(ScreenManager.templateFolder + "\DeviceHome.png", 0)
        self.templates[ScreenType.RESULT] = cv2.imread(ScreenManager.templateFolder + "\Result.png", 0)

    def GetScreen(self, screenShot):
        screenType = ScreenType.UNKNOWN
        for type in self.templates.keys():
            if self.IsMatch(screenShot.image, self.templates[type]):
                screenType = type
                break
        return Screen(screenType)

    def IsMatch(self, image, template):
        res = cv2.matchTemplate(image, template, cv2.TM_SQDIFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print("[ScreenManager] IsMatch: " + str(min_val) + " -> " + str(min_val < self.threadHold))
        return min_val < self.threadHold