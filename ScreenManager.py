import cv2
from Screen import Screen
from Screen import ScreenType

class ScreenManager:

    templateFolder = "ScreenTemplate"

    def __init__(self):
        self.threadHold = 1000
        self.deviceHomeTemplate = cv2.imread(ScreenManager.templateFolder + "\DeviceHome.png", 0)
        self.resultScreenTemplate = cv2.imread(ScreenManager.templateFolder + "\Result.png", 0)

    def GetScreen(self, screenShot):
        screenType = ScreenType.UNKNOWN
        if self.IsMatch(screenShot.image, self.deviceHomeTemplate):
            screenType = ScreenType.DEVICE_HOME
        elif self.IsMatch(screenShot.image, self.resultScreenTemplate):
            screenType = ScreenType.RESULT
        return Screen(screenType)

    def IsMatch(self, image, template):
        res = cv2.matchTemplate(image, template, cv2.TM_SQDIFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print("[ScreenManager] IsMatch: " + str(min_val) + " -> " + str(min_val < self.threadHold))
        return min_val < self.threadHold