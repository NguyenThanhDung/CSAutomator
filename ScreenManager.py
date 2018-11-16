import cv2
from Screen import Screen
from Screen import ScreenType
from TemplateImage import TemplateImage

class ScreenManager:

    def __init__(self):
        self.templates = []
        
        self.templates.append(TemplateImage(ScreenType.GAME_HOME, "GameHome_MainMenu.png"))
        self.templates.append(TemplateImage(ScreenType.MAP, "Map_GoToLobby.png", 1000000))

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
        self.templates.append(TemplateImage(ScreenType.MYSTERIOUS_SANCTUARY_LOSE, "MysteriousSanctuary_Lose.png", 100000))
        self.templates.append(TemplateImage(ScreenType.MYSTERIOUS_SANCTUARY_RESULT_LOSE, "MysteriousSanctuary_Result_Lose.png", 100000))
        self.templates.append(TemplateImage(ScreenType.PvE_GUARDIAN_PLACEMENT, "PvE_GuardianPlacement.png"))

        pve_result_victory = TemplateImage(ScreenType.PVE_RESULT_VICTORY, "PvEResult_MenuButtons.png", 100000)
        pve_result_victory.AddCriteria("PvEResult_Victory.png", 500000)
        self.templates.append(pve_result_victory)

        self.templates.append(TemplateImage(ScreenType.NOT_ENOUGH_SHOES_AT_GUARDIAN_PLACEMENT, "NotEnoughShoes_AtGuardianPlacement.png"))
        self.templates.append(TemplateImage(ScreenType.NOT_ENOUGH_SHOES_AT_RESULT, "NotEnoughShoes_AtResult.png"))

        self.templates.append(TemplateImage(ScreenType.PROMOTION_BATTLE, "PromotionBattle.png"))
        self.templates.append(TemplateImage(ScreenType.BATTLE_LIST_REFRESH_CONFIRMATION, "PromotionBattle_BattleList_RefreshConfirmation.png", 1500000))
        self.templates.append(TemplateImage(ScreenType.BATTLE_LIST_REFRESH_WITH_MOONSTONE, "PromotionBattle_BattleList_RefreshWithMoonstone.png", 1500000))
        self.templates.append(TemplateImage(ScreenType.RIVAL_LIST, "PromotionBattle_RivalList.png"))
        self.templates.append(TemplateImage(ScreenType.RIVAL_MATCH_END, "RevalMatch_End.png"))
        self.templates.append(TemplateImage(ScreenType.BATTLE_RESULT_WIN, "Battle_Result_Win.png", 1000000))
        self.templates.append(TemplateImage(ScreenType.BATTLE_RESULT_LOSE, "Battle_Result_Lose.png", 1000000))
        self.templates.append(TemplateImage(ScreenType.NOT_ENOUGH_TICKETS, "PromotionBattle_NotEnoughTickets.png", 500000))
        self.templates.append(TemplateImage(ScreenType.PROMOTION_BATTLE_GUARDIAN_PLACEMENT, "PromotionBattle_GuardianPlacement.png"))
        self.templates.append(TemplateImage(ScreenType.RIVAL_GUARDIAN_PLACEMENT, "Rival_GuardianPlacement.png"))
        
        battleRefreshReset = TemplateImage(ScreenType.BATTLE_REFRESH_RESET, "PromotionBattle_RefreshReset_Title.png", 500000)
        battleRefreshReset.AddCriteria("PromotionBattle_RefreshReset_OkButton.png")
        self.templates.append(battleRefreshReset)

        dailyMissionPopup = TemplateImage(ScreenType.DAILY_MISSION_POPUP, "DailyMission_Popup_Go.png")
        dailyMissionPopup.AddCriteria("DailyMission_Popup_Close.png")
        self.templates.append(dailyMissionPopup)

        self.templates.append(TemplateImage(ScreenType.DAILY_MISSION, "DailyChallenge.png"))
        self.templates.append(TemplateImage(ScreenType.MAIL_BOX_INBOX_TAB, "MailBox_InboxTab.png"))

        mailBox_Collect = TemplateImage(ScreenType.MAIL_BOX_COLLECT, "MailBox_CollectPopup_Title.png", 100000)
        mailBox_Collect.AddCriteria("MailBox_CollectPopup_OkButton.png")
        self.templates.append(mailBox_Collect)

        self.templates.append(TemplateImage(ScreenType.SHOP, "Shop.png", 30000))

        screenTemplate = TemplateImage(ScreenType.SHOP_DIALOG_IS_OPENNING, "Shop_DialogIsOpening.png", 30000)
        screenTemplate.AddCriteria("Shop_EquipmentInfo_Buttons.png", 30000)
        self.templates.append(screenTemplate)

        screenTemplate = TemplateImage(ScreenType.SHOP_DIALOG_PURCHASE_CONFIRMATION, "Shop_Equipment_PurchaseConfirmation.png", 30000)
        screenTemplate.AddCriteria("Shop_Equipment_PurchaseConfirmation_OK.png")
        screenTemplate.AddCriteria("Shop_Equipment_PurchaseConfirmation_Cancel.png")
        self.templates.append(screenTemplate)

        self.templates.append(TemplateImage(ScreenType.SUMMON, "Summon.png"))
        self.templates.append(TemplateImage(ScreenType.SUMMON_BASIC_DONE, "Summon_BasicDone.png"))
        self.templates.append(TemplateImage(ScreenType.SUMMON_MYSTEROUS_DONE, "Summon_MysteriousDone.png"))
        self.templates.append(TemplateImage(ScreenType.SUMMON_LEGEND_DONE, "Summon_LegendDone.png"))

        self.templates.append(TemplateImage(ScreenType.EVENT_DUNGEON, "EventDungeon.png"))
        self.templates.append(TemplateImage(ScreenType.EVENT_DUNGEON_RESULT_EXP, "EventDungeon_Result_EXP.png"))
        self.templates.append(TemplateImage(ScreenType.EVENT_DUNGEON_RESULT_GOLD, "EventDungeon_Result_Gold.png"))

        self.templates.append(TemplateImage(ScreenType.DEVICE_HOME, "DeviceHome.png"))
        self.templates.append(TemplateImage(ScreenType.TAP_TO_START, "TapToStart.png", 1000))
        self.templates.append(TemplateImage(ScreenType.EVENT_INFO_1, "EventInfo1.png"))
        self.templates.append(TemplateImage(ScreenType.EVENT_INFO_2, "EventInfo2.png"))
        self.templates.append(TemplateImage(ScreenType.EVENT_INFO_3, "EventInfo3.png"))
        self.templates.append(TemplateImage(ScreenType.DIALOG_WEEKLY_LIMITED, "WeeklyLimited.png"))
        self.templates.append(TemplateImage(ScreenType.DIALOG_LIMITED_OFFER, "LimitedOffer.png"))
        self.templates.append(TemplateImage(ScreenType.DIALOG_SUGGESTED_ITEM, "Dialog_SuggestedItem.png", 100000))
        self.templates.append(TemplateImage(ScreenType.DIALOG_SHOES_RECHARGE_FP, "Dialog_ShoesRecharge.png", 100000))
        self.templates.append(TemplateImage(ScreenType.DIALOG_SHOES_RECHARGE_II, "Dialog_ShoesRechargeII.png", 100000))
        self.templates.append(TemplateImage(ScreenType.DIALOG_NOT_ENOUGH_FP, "Dialog_NotEnoughFP.png", 100000))
        self.templates.append(TemplateImage(ScreenType.DIALOG_PURCHASE_COMPLETE, "Dialog_PurchaseComplete.png", 1000000))
        self.templates.append(TemplateImage(ScreenType.DAILY_LOGIN_REWARD, "DailyLoginReward.png", 1000000))

        screenTemplate = TemplateImage(ScreenType.EVENT_DUNGEON_OUT_OF_ENTRANCE_POPUP, "EventDungeon_PopUpIsOpening.png", 100000)
        screenTemplate.AddCriteria("EventDungeon_OutOfEntrancePopUp.png", 1000000)
        self.templates.append(screenTemplate)
        
        unstableNetworkDialog = TemplateImage(ScreenType.DIALOG_UNSTABLE_NETWORK, "UnstableNetwork_Title.png", 10000000)
        unstableNetworkDialog.AddCriteria("UnstableNetwork_YesButton.png", 1000000)
        unstableNetworkDialog.AddCriteria("UnstableNetwork_NoButton.png", 1000000)
        self.templates.append(unstableNetworkDialog)
        
        self.templates.append(TemplateImage(ScreenType.BATTLE_NEW_SEASON, "Battle_NewSeason.png"))
        self.templates.append(TemplateImage(ScreenType.BATTLE_PREPARING_NEW_SEASON, "PromotionBattle_PreparingForNewSeason.png"))
        
        self.templates.append(TemplateImage(ScreenType.BATTLE_RANKING, "Battle_Ranking.png"))
        self.templates.append(TemplateImage(ScreenType.BATTLE_DEFENSE_RECORD, "Battle_DefenseRecord.png"))

        self.templates.append(TemplateImage(ScreenType.PVE_RESULT_REPEAT_RESULT, "PvEResult_RepeatBattleResult.png", 100000))
        self.templates.append(TemplateImage(ScreenType.LEVEL_UP, "LevelUp.png"))

    def GetScreen(self, screenShot):
        screenType = ScreenType.UNKNOWN
        image = None
        for template in self.templates:
            if template.IsMatch(screenShot) == True:
                screenType = template.screenType
                image = screenShot.image
                break
        return Screen(screenType, image)