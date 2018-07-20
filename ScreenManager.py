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
        gameHome.AddCriteria("GameHome_EventMailChatButtons.png", 1000000)
        gameHome.AddCriteria("GameHome_Gold.png", 1000000)
        gameHome.AddCriteria("GameHome_MoonStone.png", 1000000)
        gameHome.AddCriteria("GameHome_Shoes.png", 1000000)
        gameHome.AddCriteria("GameHome_BattleTickets.png", 1000000)
        self.templates.append(gameHome)

        map = TemplateImage(ScreenType.MAP, "Map_GoToLobby.png", 1000000)
        map.AddCriteria("Map_MysteriousSanctuary.png", 1000000)
        map.AddCriteria("Map_UnknownLand.png", 1000000)
        self.templates.append(map)
        
        self.templates.append(TemplateImage(ScreenType.MYSTERIOUS_SANCTUARY, "MysteriousSanctuary.png"))
        self.templates.append(TemplateImage(ScreenType.SHRINE_OF_LIGHT, "ShrineOfLight.png"))
        self.templates.append(TemplateImage(ScreenType.GUARDIAN_PLACEMENT, "GuardianPlacement.png"))

        actionPhase = TemplateImage(ScreenType.ACTION_PHASE, "ActionPhase_AutoPlayButton.png", 1000000)
        actionPhase.AddCriteria("ActionPhase_ChatButton.png", 1000000)
        actionPhase.AddCriteria("ActionPhase_HelpButton.png", 1000000)
        actionPhase.AddCriteria("ActionPhase_SettingButton.png", 1000000)
        actionPhase.AddCriteria("ActionPhase_x2Button.png", 1000000)
        self.templates.append(actionPhase)

        pve_result_victory = TemplateImage(ScreenType.PVE_RESULT_VICTORY, "PvEResult_MenuButtons.png")
        pve_result_victory.AddCriteria("PvEResult_Victory.png")
        self.templates.append(pve_result_victory)

        self.templates.append(TemplateImage(ScreenType.NOT_ENOUGH_SHOES, "NotEnoughShoes.png"))
        self.templates.append(TemplateImage(ScreenType.RESULT, "Result.png"))

    def GetScreen(self, screenShot):
        screenType = ScreenType.UNKNOWN
        for template in self.templates:
            result = template.FindMatch(screenShot)
            if result.isMatch == True:
                screenType = template.screenType
                break
        return Screen(screenType, result.location)