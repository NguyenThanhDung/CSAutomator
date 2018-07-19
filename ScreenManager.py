import cv2
from Screen import Screen
from Screen import ScreenType
from TemplateImage import TemplateImage

class ScreenManager:

    def __init__(self):
        self.templates = []
        self.templates.append(TemplateImage(ScreenType.DEVICE_HOME, "DeviceHome.png"))
        self.templates.append(TemplateImage(ScreenType.TAP_TO_START, "TapToStart.png"))
        self.templates.append(TemplateImage(ScreenType.EVENT_INFO, "EventInfo.png", 120000))
        self.templates.append(TemplateImage(ScreenType.DAILY_LOGIN_REWARD, "DailyLoginReward.png", 6000))
        
        gameHome = TemplateImage(ScreenType.GAME_HOME, "GameHome_MainMenu.png", 30000000)
        gameHome.AddCriteria("GameHome_EventMailChatButtons.png", 500000)
        gameHome.AddCriteria("GameHome_Gold.png", 500000)
        gameHome.AddCriteria("GameHome_MoonStone.png", 500000)
        gameHome.AddCriteria("GameHome_Shoes.png", 500000)
        gameHome.AddCriteria("GameHome_BattleTickets.png", 500000)
        self.templates.append(gameHome)
        
        self.templates.append(TemplateImage(ScreenType.RESULT, "Result.png"))

    def GetScreen(self, screenShot):
        screenType = ScreenType.UNKNOWN
        for template in self.templates:
            result = template.FindMatch(screenShot)
            if result.isMatch == True:
                screenType = template.screenType
                break
        return Screen(screenType, result.location)