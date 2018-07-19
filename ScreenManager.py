import cv2
from Screen import Screen
from Screen import ScreenType
from TemplateImage import TemplateImage

class ScreenManager:

    templateFolder = "ScreenTemplate"
    defaultPrecisionThreadhold = 1000

    def __init__(self):
        self.templates = []
        self.templates.append(TemplateImage(ScreenType.DEVICE_HOME, ScreenManager.templateFolder + "\DeviceHome.png"))
        self.templates.append(TemplateImage(ScreenType.TAP_TO_START, ScreenManager.templateFolder + "\TapToStart.png"))
        self.templates.append(TemplateImage(ScreenType.EVENT_INFO, ScreenManager.templateFolder + "\EventInfo.png", 120000))
        self.templates.append(TemplateImage(ScreenType.DAILY_LOGIN_REWARD, ScreenManager.templateFolder + "\DailyLoginReward.png", 6000))
        self.templates.append(TemplateImage(ScreenType.GAME_HOME, ScreenManager.templateFolder + "\GameHome.png"))
        self.templates.append(TemplateImage(ScreenType.RESULT, ScreenManager.templateFolder + "\Result.png"))

    def GetScreen(self, screenShot):
        screenType = ScreenType.UNKNOWN
        for template in self.templates:
            result = template.FindMatch(screenShot)
            if result.isMatch == True:
                screenType = template.screenType
                break
        return Screen(screenType, result.location)