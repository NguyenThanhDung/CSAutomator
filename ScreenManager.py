import cv2
from Screen import Screen
from Screen import ScreenType
from TemplateImage import TemplateImage

class ScreenManager:

    def __init__(self):
        self.templates = []
        
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

        promotionBattle_RewardInfo = TemplateImage(ScreenType.REWARD_INFO, "RewardInfo_Title.png", 20000)
        promotionBattle_RewardInfo.AddCriteria("RewardInfo_OkButton.png")
        self.templates.append(promotionBattle_RewardInfo)
        
        self.templates.append(TemplateImage(ScreenType.MYSTERIOUS_SANCTUARY, "MysteriousSanctuary.png"))
        self.templates.append(TemplateImage(ScreenType.SHRINE_OF_LIGHT, "ShrineOfLight.png"))
        self.templates.append(TemplateImage(ScreenType.GUARDIAN_PLACEMENT, "GuardianPlacement.png"))

        pve_result_victory = TemplateImage(ScreenType.PVE_RESULT_VICTORY, "PvEResult_MenuButtons.png")
        pve_result_victory.AddCriteria("PvEResult_Victory.png")
        self.templates.append(pve_result_victory)

        self.templates.append(TemplateImage(ScreenType.NOT_ENOUGH_SHOES, "NotEnoughShoes.png", 300000))

        self.templates.append(TemplateImage(ScreenType.BATTLE_LIST, "PromotionBattle_BattleList.png"))
        self.templates.append(TemplateImage(ScreenType.BATTLE_LIST_REFRESH_CONFIRMATION, "PromotionBattle_BattleList_RefreshConfirmation.png", 1500000))
        self.templates.append(TemplateImage(ScreenType.BATTLE_LIST_REFRESH_WITH_MOONSTONE, "PromotionBattle_BattleList_RefreshWithMoonstone.png", 1500000))
        self.templates.append(TemplateImage(ScreenType.RIVAL_LIST, "PromotionBattle_RivalList.png"))
        self.templates.append(TemplateImage(ScreenType.RIVAL_MATCH_END, "RevalMatch_End.png"))
        self.templates.append(TemplateImage(ScreenType.BATTLE_RESULT_WIN, "Battle_Result_Win.png"))
        self.templates.append(TemplateImage(ScreenType.BATTLE_RESULT_LOSE, "Battle_Result_Lose.png"))
        self.templates.append(TemplateImage(ScreenType.NOT_ENOUGH_TICKETS, "PromotionBattle_NotEnoughTickets.png", 500000))
        
        battleRefreshReset = TemplateImage(ScreenType.BATTLE_REFRESH_RESET, "PromotionBattle_RefreshReset_Title.png", 100000)
        battleRefreshReset.AddCriteria("PromotionBattle_RefreshReset_OkButton.png")
        self.templates.append(battleRefreshReset)

        self.templates.append(TemplateImage(ScreenType.DAILY_MISSION, "DailyChallenge.png"))
        self.templates.append(TemplateImage(ScreenType.MAIL_BOX_INBOX_TAB, "MailBox_InboxTab.png"))

        mailBox_Collect = TemplateImage(ScreenType.MAIL_BOX_COLLECT, "MailBox_CollectPopup_Title.png", 100000)
        mailBox_Collect.AddCriteria("MailBox_CollectPopup_OkButton.png")
        self.templates.append(mailBox_Collect)

        self.templates.append(TemplateImage(ScreenType.DEVICE_HOME, "DeviceHome.png", 30000))
        self.templates.append(TemplateImage(ScreenType.TAP_TO_START, "TapToStart.png", 100000))
        self.templates.append(TemplateImage(ScreenType.EVENT_INFO, "EventInfo.png", 120000))
        self.templates.append(TemplateImage(ScreenType.DAILY_LOGIN_REWARD, "DailyLoginReward.png", 100000))
        self.templates.append(TemplateImage(ScreenType.BATTLE_NEW_SEASON, "Battle_NewSeason.png", 100000))
        self.templates.append(TemplateImage(ScreenType.BATTLE_RANKING, "Battle_Ranking.png"))

    def GetScreen(self, screenShot):
        screenType = ScreenType.UNKNOWN
        image = None
        for template in self.templates:
            if template.IsMatch(screenShot) == True:
                screenType = template.screenType
                image = screenShot.image
                break
        return Screen(screenType, image)