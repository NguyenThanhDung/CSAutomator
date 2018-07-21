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

        actionPhase_PlayButtonEnabled = TemplateImage(ScreenType.ACTION_PHASE_PLAY_ENABLED, "ActionPhase_AutoPlayButton_Enabled.png", 1000000)
        actionPhase_PlayButtonEnabled.AddCriteria("ActionPhase_ChatButton.png", 1000000)
        actionPhase_PlayButtonEnabled.AddCriteria("ActionPhase_HelpButton.png", 1000000)
        actionPhase_PlayButtonEnabled.AddCriteria("ActionPhase_SettingButton.png", 1000000)
        actionPhase_PlayButtonEnabled.AddCriteria("ActionPhase_x2Button.png", 1000000)
        self.templates.append(actionPhase_PlayButtonEnabled)

        actionPhase_PlayButtonDisabled = TemplateImage(ScreenType.ACTION_PHASE_PLAY_DISABLED, "ActionPhase_AutoPlayButton_Disables.png", 1000000)
        actionPhase_PlayButtonDisabled.AddCriteria("ActionPhase_ChatButton.png", 1000000)
        actionPhase_PlayButtonDisabled.AddCriteria("ActionPhase_HelpButton.png", 1000000)
        actionPhase_PlayButtonDisabled.AddCriteria("ActionPhase_SettingButton.png", 1000000)
        actionPhase_PlayButtonDisabled.AddCriteria("ActionPhase_x2Button.png", 1000000)
        self.templates.append(actionPhase_PlayButtonDisabled)
        
        self.templates.append(TemplateImage(ScreenType.MYSTERIOUS_SANCTUARY, "MysteriousSanctuary.png"))
        self.templates.append(TemplateImage(ScreenType.SHRINE_OF_LIGHT, "ShrineOfLight.png"))
        self.templates.append(TemplateImage(ScreenType.GUARDIAN_PLACEMENT, "GuardianPlacement.png"))

        pve_result_victory = TemplateImage(ScreenType.PVE_RESULT_VICTORY, "PvEResult_MenuButtons.png")
        pve_result_victory.AddCriteria("PvEResult_Victory.png")
        self.templates.append(pve_result_victory)

        self.templates.append(TemplateImage(ScreenType.NOT_ENOUGH_SHOES, "NotEnoughShoes.png"))

        self.templates.append(TemplateImage(ScreenType.BATTLE_LIST, "PromotionBattle_BattleList.png"))
        self.templates.append(TemplateImage(ScreenType.BATTLE_LIST_REFRESH_CONFIRMATION, "PromotionBattle_BattleList_RefreshConfirmation.png"))

        promotionBattle_RivalList_Available = TemplateImage(ScreenType.RIVAL_LIST_AVAILABLE, "PromotionBattle_RivalList_Main.png")
        promotionBattle_RivalList_Available.AddCriteria("PromotionBattle_RivalList_Available.png")
        self.templates.append(promotionBattle_RivalList_Available)

        promotionBattle_RivalList_NotAvailable = TemplateImage(ScreenType.RIVAL_LIST_NOT_AVAILABLE, "PromotionBattle_RivalList_Main.png")
        promotionBattle_RivalList_NotAvailable.AddCriteria("PromotionBattle_RivalList_NotAvailable.png")
        self.templates.append(TemplateImage(ScreenType.RIVAL_LIST_NOT_AVAILABLE, "PromotionBattle_RivalList_Main.png"))

        self.templates.append(TemplateImage(ScreenType.RIVAL_MATCH_END, "RevalMatch_End.png"))
        self.templates.append(TemplateImage(ScreenType.BATTLE_RESULT, "Battle_Result.png"))

    def GetScreen(self, screenShot):
        screenType = ScreenType.UNKNOWN
        image = None
        for template in self.templates:
            if template.IsMatch(screenShot) == True:
                screenType = template.screenType
                image = screenShot.image
                break
        return Screen(screenType, image)