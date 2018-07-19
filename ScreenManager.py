import cv2
from Screen import Screen
from Screen import ScreenType
from TemplateImage import TemplateImage

class ScreenManager:

    def __init__(self):
        self.templates = []
        self.templates.append(TemplateImage(ScreenType.DEVICE_HOME, "DeviceHome.png", 1000))
        self.templates.append(TemplateImage(ScreenType.TAP_TO_START, "TapToStart.png", 1000))
        self.templates.append(TemplateImage(ScreenType.EVENT_INFO, "EventInfo.png", 120000))
        self.templates.append(TemplateImage(ScreenType.DAILY_LOGIN_REWARD, "DailyLoginReward.png", 6000))
        
        gameHome = TemplateImage(ScreenType.GAME_HOME, "GameHome_MainMenu.png", 30000000)
        gameHome.AddCriteria("GameHome_EventMailChatButtons.png")
        gameHome.AddCriteria("GameHome_Gold.png")
        gameHome.AddCriteria("GameHome_MoonStone.png")
        gameHome.AddCriteria("GameHome_Shoes.png")
        gameHome.AddCriteria("GameHome_BattleTickets.png")
        self.templates.append(gameHome)
        
        self.templates.append(TemplateImage(ScreenType.RESULT, "Result.png", 1000))

    def GetScreen(self, screenShot):
        screenType = ScreenType.UNKNOWN
        for template in self.templates:
            result = template.FindMatch(screenShot)
            if result.isMatch == True:
                screenType = template.screenType
                break
        return Screen(screenType, result.location)