import time
from enum import Enum
from Screen import ScreenType
from ButtonPositions import ButtonPositions, Button, Position
from Equipment import Equipment
from Prorfile import Profile, ProfileField

class GameState(Enum):
    NONE = 0
    DAILY_MISSION = 1
    PROMOTION_BATTLE = 2
    MYSTERIOUS_SANCTUARY = 3
    OUT_OF_SHOES = 4

class ShoesSource(Enum):
    DAILY_MISSION_REWARD = 0
    MAIL_BOX = 1
    SHOP_WITH_FP = 2
    SHOP_WITH_MOONSTONE = 3

class DailyMission(Enum):
    NONE = 0
    POWER_UP_GUARDIAN = 1
    SUMMON_GUARDIAN = 2
    POWER_UP_EQUIPMENT = 3
    DISASSEMBLY = 4
    DEAR_FRIEND = 5

class GameManager:

    def __init__(self, device, profile):
        self.device = device
        self.profile = profile
        self.screen = None
        self.gameState = GameState.PROMOTION_BATTLE
        self.shoesSource = ShoesSource.DAILY_MISSION_REWARD
        self.dailMissionState = DailyMission.NONE
        self.scrollStep = 0

    def SetScreen(self, screen):
        self.screen = screen

    def Play(self):
        if self.screen.screenType == ScreenType.DEVICE_HOME:
            iconLocation = self.screen.Find("DeviceHome.png", 30000)
            if iconLocation is not None:
                print("[GameManager] Start game")
                self.device.Touch(iconLocation[0] + 5, iconLocation[1] + 5)
                time.sleep(5)
                self.device.LoadDeviceInfo()
            else:
                print("[GameManager] Can not find the game icon!")
        elif self.screen.screenType == ScreenType.TAP_TO_START:
            print("[GameManager] Tap to start...")
            self.device.Touch(640, 360)
        elif self.screen.screenType == ScreenType.EVENT_INFO:
            print("[GameManager] Close event information dialog")
            self.device.Touch(1215, 630)
        elif self.screen.screenType == ScreenType.DIALOG_WEEKLY_LIMITED    \
            or self.screen.screenType == ScreenType.DIALOG_LIMITED_OFFER:
            print("[GameManager] Close dialog")
            self.device.Touch(344, 38)
        elif self.screen.screenType == ScreenType.DIALOG_SUGGESTED_ITEM:
            print("[GameManager] Close dialog")
            self.device.Touch(960, 448)
        elif self.screen.screenType == ScreenType.DAILY_LOGIN_REWARD:
            print("[GameManager] Close dayly log-gin reward")
            self.device.Touch(974, 357)
        elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_DISABLED:
            print("[GameManager] Enable auto play")
            self.device.Touch(58, 107)
        elif self.screen.screenType == ScreenType.REWARD_INFO:
            print("[GameManager] Press OK")
            self.device.Touch(797, 356)
        elif self.screen.screenType == ScreenType.BATTLE_LIST_REFRESH_CONFIRMATION:
            print("[GameManager] Confirm refresh")
            self.device.Touch(784, 243)
        elif self.screen.screenType == ScreenType.BATTLE_LIST_REFRESH_WITH_MOONSTONE:
            print("[GameManager] Don't refresh with moonstone")
            self.device.Touch(784, 474)
        elif self.screen.screenType == ScreenType.BATTLE_RESULT_WIN \
            or self.screen.screenType == ScreenType.BATTLE_RESULT_LOSE:
            print("[GameManager] Press Exit")
            self.device.Touch(1196, 115)
        elif self.screen.screenType == ScreenType.RIVAL_MATCH_END:
            print("[GameManager] Press Skip")
            self.device.Touch(1223, 58)
        elif self.screen.screenType == ScreenType.BATTLE_REFRESH_RESET:
            print("[GameManager] OK")
            self.device.Touch(784, 357)
        elif self.screen.screenType == ScreenType.NOT_ENOUGH_TICKETS:
            print("[GameManager] Go to Mysterious Sanctuary...")
            self.gameState = GameState.MYSTERIOUS_SANCTUARY
            self.device.Touch(788, 471)
            self.device.Touch(40, 48)
        elif self.screen.screenType == ScreenType.DIALOG_PURCHASE_COMPLETE:
            print("[GameManager] Close dialog. Go to battle...")
            self.gameState = GameState.PROMOTION_BATTLE
            self.shoesSource = ShoesSource.DAILY_MISSION_REWARD
            self.device.Touch(783, 355)
            self.device.Touch(40, 48)
        elif self.screen.screenType == ScreenType.BATTLE_NEW_SEASON:
            print("[GameManager] OK")
            self.device.Touch(784, 358)
        elif self.screen.screenType == ScreenType.MAIL_BOX_COLLECT:
            print("[GameManager] OK")
            self.device.Touch(799, 357)
        elif self.screen.screenType == ScreenType.DIALOG_UNSTABLE_NETWORK:
            print("[GameManager] Yes")
            self.device.Touch(788, 244)
        elif self.screen.screenType == ScreenType.GAME_HOME:
            screenPiece = self.screen.Find("GameHome_SummonAvailable.png")
            if screenPiece is not None:
                print("[GameManager] Summon available. Go to summon...")
                self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Home_Summon))
            else:
                if self.profile.GetField(ProfileField.DidPlayEventDungeon) == False:
                    screenPiece = self.screen.Find("GameHome_EventDungeon.png")
                    if screenPiece is not None:
                        print("[GameManager] Open Event Dungeon")
                        self.device.Touch(screenPiece[0] + 10, screenPiece[1] + 10)
                    else:
                        print("[GameManager] Can't find Event Dungeon button. Continue...")
                        self.PlaySubstate()
                else:
                    print("[GameManager] There isn't any special event. Continue...")
                    self.PlaySubstate()
        elif self.screen.screenType == ScreenType.SUMMON:
            print("[GameManager] Summon...")
            self.Summon()
        elif self.screen.screenType == ScreenType.EVENT_DUNGEON:
            screenPiece = self.screen.Find("EventDungeon_EXP_OutOfEntrance.png", 100000)
            if screenPiece is not None:
                print("[GameManager] EXP Dungeon is out of entrance. Go home...")
                self.profile.SetField(ProfileField.DidPlayEventDungeon, True)
                self.profile.Save()
                self.GoHome()
            else:
                # TODO: WIP
                screenPiece = self.screen.Find("WeeklyLimited.png")
                if screenPiece is not None:
                    print("[GameManager] Gold Dungeon is out of entrance. Go home...")
                    self.profile.SetField(ProfileField.DidPlayEventDungeon, True)
                    self.profile.Save()
                    self.GoHome()
                else:
                    screenPiece = self.screen.Find("EventDungeon_EXP.png", 100000)
                    if screenPiece is not None:
                        print("[GameManager] Play EXP Dungeon")
                        self.device.Touch(screenPiece[0] + 10, screenPiece[1] + 10)
                    else:
                        self.PlaySubstate()
        elif self.screen.screenType == ScreenType.EVENT_DUNGEON_RESULT:
            print("[GameManager] Stop")
            self.device.Touch(1195, 120)
        else:
            self.PlaySubstate()

    def PlaySubstate(self):
        if self.gameState == GameState.DAILY_MISSION:
            self.PlayDailyMission()
        elif self.gameState == GameState.PROMOTION_BATTLE:
            self.PlayPromotionBattle()
        elif self.gameState == GameState.MYSTERIOUS_SANCTUARY:
            self.PlayMysteriousSanctuary()
        elif self.gameState == GameState.OUT_OF_SHOES:
            self.FindShoes()
        else:
            self.GoHome()

    def PlayDailyMission(self):
        if self.dailMissionState == DailyMission.NONE:
            if self.screen.screenType == ScreenType.GAME_HOME:
                print("[GameManager] Open daily mission reward")
                self.device.Touch(1184, 634)
                time.sleep(1)
                self.device.Touch(756, 82)
                self.scrollStep = 0
            elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_ENABLED:
                print("[GameManager] Idle in 20 seconds...")
                time.sleep(20)
            elif self.screen.screenType == ScreenType.NOT_ENOUGH_SHOES:
                print("[GameManager] Idle")
            elif self.screen.screenType == ScreenType.DAILY_MISSION:
                mission = self.screen.Find("DailyMission_Disassembly.png")
                if mission is not None:
                    print("[GameManager] Open mission")
                    self.dailMissionState = DailyMission.DISASSEMBLY
                    self.device.Touch(mission[0] + 64, mission[1] + 240)
                    return
                mission = self.screen.Find("DailyMission_DearFriend.png")
                if mission is not None:
                    self.dailMissionState = DailyMission.DEAR_FRIEND
                    self.GoHome()
                    return
            elif self.screen.screenType == ScreenType.MAIL_BOX_INBOX_TAB:
                print("[GameManager] Close mail box")
                self.device.Touch(51, 40)
            else:
                self.GoHome()
        elif self.dailMissionState == DailyMission.DISASSEMBLY:
            if self.screen.screenType == ScreenType.DAILY_MISSION_POPUP:
                print("[GameManager] Go to play mission...")
                self.device.Touch(785, 460)
            else:
                print("[GameManager] Idle")
        elif self.dailMissionState == DailyMission.DEAR_FRIEND:
            if self.screen.screenType == ScreenType.GAME_HOME:
                print("[GameManager] Open Community")
                self.device.Touch(1183, 634)
                time.sleep(1)
                self.device.Touch(891, 632)
            else:
                print("[GameManager] Idle")
        else:
            print("[GameManager] Idle")
    
    def PlayPromotionBattle(self):
        if self.screen.screenType == ScreenType.GAME_HOME:
            print("[GameManager] Open map")
            self.device.Touch(1174, 360)
        elif self.screen.screenType == ScreenType.MAP:
            print("[GameManager] Open Promotion Battle")
            self.device.Touch(1077, 547)
        elif self.screen.screenType == ScreenType.GUARDIAN_PLACEMENT:
            print("[GameManager] Auto place and start")
            self.device.Touch(767, 627)
            self.device.Touch(765, 141)
        elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_ENABLED:
            print("[GameManager] Idle in 20 seconds...")
            time.sleep(20)
        elif self.screen.screenType == ScreenType.NOT_ENOUGH_SHOES:
            self.gameState = GameState.OUT_OF_SHOES
            self.device.Touch(790, 474)
            if self.screen.Find("NotEnoughShoes_At_GuardianPlacement.png") is not None:
                print("[GameManager] Not enough shoes at guardian placement. Find more shoes...")
                self.device.Touch(46, 51)
            elif self.screen.Find("NotEnoughShoes_At_Result.png") is not None:
                print("[GameManager] Not enough shoes at result. Find more shoes...")
                self.device.Touch(1197, 663)
            else:
                print("[GameManager] Not enough shoes. Close the pop-up")
        elif self.screen.screenType == ScreenType.BATTLE_LIST:
            if self.screen.Find("PromotionBattle_BattleList_RivalAvailable.png") is not None:
                print("[GameManager] Rival available. Switch to Rival list")
                self.device.Touch(1221, 505)
            else:
                potentialMatch = self.screen.Find("PromotionBattle_BattleList_PotentialMatch.png")
                if potentialMatch is not None:
                    print("[GameManager] There is a potential match, go for battle")
                    self.scrollStep = 0
                    self.device.Touch(potentialMatch[0] + 40, potentialMatch[1] + 70)
                else:
                    if self.scrollStep < 2:
                        print("[GameManager] Can not find any potential match, scroll up")
                        self.device.Swipe(1016, 226, 614, 226)
                        self.scrollStep = self.scrollStep + 1
                    else:
                        self.scrollStep = 0
                        refreshAvailable = self.screen.Find("PromotionBattle_BattleList_RefreshAvailable.png")
                        if refreshAvailable is not None:
                            print("[GameManager] There isn't any potential match, refresh list")
                            self.device.Swipe(569, 226, 1116, 226)
                            self.device.Swipe(569, 226, 1116, 226)
                            self.device.Touch(514, 108)
                        else:
                            print("[GameManager] There isn't any potential match, refresh is not available, go to Mysterious Sanctuary")
                            self.gameState = GameState.MYSTERIOUS_SANCTUARY
        elif self.screen.screenType == ScreenType.RIVAL_LIST:
            rivalAvailable = self.screen.Find("PromotionBattle_RivalList_Available.png")
            if rivalAvailable is not None:
                print("[GameManager] Start Rival match...")
                batteButtonLocaltion = self.screen.Find("PromotionBattle_RivalList_BattleButton.png")
                if batteButtonLocaltion is not None:
                    print("[GameManager] Press Battle button at " + str(batteButtonLocaltion))
                    self.device.Touch(batteButtonLocaltion[0] + 5, batteButtonLocaltion[1] + 5)
                else:
                    print("[GameManager] Schroll down")
                    self.device.Swipe(1116, 351, 569, 351)
            else:
                battleAvailable = self.screen.Find("PromotionBattle_BattleAvailable.png")
                if battleAvailable is not None:
                    print("[GameManager] Switch to Battle tab")
                    self.device.Touch(battleAvailable[0] + 52, battleAvailable[1] + 44)
                else:
                    print("[GameManager] Go home")
                    self.device.Touch(38, 46)
        elif self.screen.screenType == ScreenType.BATTLE_RANKING:
            rivalAvailable = self.screen.Find("PromotionBattle_BattleList_RivalAvailable.png")
            if rivalAvailable is not None:
                print("[GameManager] Switch to Rival tab")
                self.device.Touch(rivalAvailable[0] + 62, rivalAvailable[1] + 66)
            else:
                battleAvailable = self.screen.Find("PromotionBattle_BattleAvailable.png")
                if battleAvailable is not None:
                    print("[GameManager] Switch to Battle tab")
                    self.device.Touch(battleAvailable[0] + 52, battleAvailable[1] + 44)
                else:
                    print("[GameManager] Play Mysterious Sanctuary...")
                    self.gameState = GameState.MYSTERIOUS_SANCTUARY
                    self.device.Touch(38, 46)
        elif self.screen.screenType == ScreenType.BATTLE_DEFENSE_RECORD:
            rivalAvailable = self.screen.Find("PromotionBattle_BattleList_RivalAvailable.png")
            if rivalAvailable is not None:
                print("[GameManager] Switch to Rival tab")
                self.device.Touch(rivalAvailable[0] + 62, rivalAvailable[1] + 66)
            else:
                battleAvailable = self.screen.Find("PromotionBattle_BattleAvailable.png")
                if battleAvailable is not None:
                    print("[GameManager] Switch to Battle tab")
                    self.device.Touch(battleAvailable[0] + 52, battleAvailable[1] + 44)
                else:
                    print("[GameManager] Go home")
                    self.device.Touch(38, 46)
        else:
            self.GoHome()
    
    def PlayMysteriousSanctuary(self):
        if self.screen.screenType == ScreenType.GAME_HOME:
            print("[GameManager] Open map")
            self.device.Touch(1174, 360)
        elif self.screen.screenType == ScreenType.MAP:
            print("[GameManager] Open Mysterious Sanctuary")
            self.device.Touch(630, 600)
        elif self.screen.screenType == ScreenType.MYSTERIOUS_SANCTUARY:
            print("[GameManager] Open Shrine of Light")
            self.device.Touch(400, 560)
        elif self.screen.screenType == ScreenType.SHRINE_OF_LIGHT:
            print("[GameManager] Open floor 7F")
            self.device.Touch(1123, 120)
        elif self.screen.screenType == ScreenType.GUARDIAN_PLACEMENT:
            print("[GameManager] Auto place and start")
            self.device.Touch(767, 627)
            self.device.Touch(765, 141)
        elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_ENABLED:
            #print("[GameManager] Idle in 2 minutes...")
            #time.sleep(120)
            print("[GameManager] Auto touch...")
            self.AutoTouch(10)
        elif self.screen.screenType == ScreenType.PVE_RESULT_VICTORY:
            print("[GameManager] Replay")
            self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Result_Replay))
        elif self.screen.screenType == ScreenType.NOT_ENOUGH_SHOES:
            self.gameState = GameState.OUT_OF_SHOES
            self.device.Touch(790, 474)
            if self.screen.Find("NotEnoughShoes_At_GuardianPlacement.png") is not None:
                print("[GameManager] Not enough shoes at guardian placement. Find more shoes...")
                self.device.Touch(46, 51)
            elif self.screen.Find("NotEnoughShoes_At_Result.png") is not None:
                print("[GameManager] Not enough shoes at result. Find more shoes...")
                self.device.Touch(1197, 663)
            else:
                print("[GameManager] Not enough shoes. Close the pop-up")
        else:
            self.GoHome()

    def FindShoes(self):
        if self.screen.screenType == ScreenType.GAME_HOME:
            if self.shoesSource == ShoesSource.DAILY_MISSION_REWARD:
                print("[GameManager] Open daily mission reward")
                self.device.Touch(1184, 634)
                time.sleep(1)
                self.device.Touch(756, 82)
                self.scrollStep = 0
            elif self.shoesSource == ShoesSource.MAIL_BOX:
                print("[GameManager] Open mail box")
                self.device.Touch(137, 52)
            elif self.shoesSource == ShoesSource.SHOP_WITH_FP:
                print("[GameManager] Open shop")
                self.device.Touch(1193, 224)
        elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_ENABLED:
            print("[GameManager] Idle in 20 seconds...")
            time.sleep(20)
        elif self.screen.screenType == ScreenType.NOT_ENOUGH_SHOES:
            self.gameState = GameState.OUT_OF_SHOES
            self.device.Touch(790, 474)
            if self.screen.Find("NotEnoughShoes_At_GuardianPlacement.png") is not None:
                print("[GameManager] Not enough shoes at guardian placement. Find more shoes...")
                self.device.Touch(46, 51)
            elif self.screen.Find("NotEnoughShoes_At_Result.png") is not None:
                print("[GameManager] Not enough shoes at result. Find more shoes...")
                self.device.Touch(1197, 663)
            else:
                print("[GameManager] Not enough shoes. Close the pop-up")
        elif self.screen.screenType == ScreenType.DAILY_MISSION:
            collectButton = self.screen.Find("DailyChallenge_CollectButton.png")
            if collectButton is not None:
                print("[GameManager] Collect reward")
                self.device.Touch(collectButton[0] + 34, collectButton[1] + 66)
            else:
                if self.scrollStep < 2:
                    print("[GameManager] Can not find any reward, scroll up")
                    self.device.Swipe(1158, 273, 265, 273)
                    self.scrollStep = self.scrollStep + 1
                else:
                    print("[GameManager] Collected all rewards, go to battle...")
                    self.gameState = GameState.PROMOTION_BATTLE
                    self.shoesSource = ShoesSource.MAIL_BOX
                    self.device.Touch(40, 48)
        elif self.screen.screenType == ScreenType.DAILY_MISSION_POPUP:
            print("[GameManager] Close pop up")
            self.device.Touch(436, 103)
        elif self.screen.screenType == ScreenType.MAIL_BOX_INBOX_TAB:
            collectButton = self.screen.Find("MailBox_CollectButton.png", 10000)
            if collectButton is not None:
                print("[GameManager] Collect reward")
                self.device.Touch(299, 57)
                self.gameState = GameState.PROMOTION_BATTLE
            else:
                print("[GameManager] Mail box is empty. Close mail box, go to shop...")
                self.shoesSource = ShoesSource.SHOP_WITH_FP
                self.device.Touch(51, 40)
        elif self.screen.screenType == ScreenType.SHOP:
            if self.shoesSource == ShoesSource.SHOP_WITH_FP:
                print("[GameManager] Buy shoes with FP")
                self.device.Swipe(924, 118, 924, 591)
                time.sleep(1)
                self.device.Touch(1063, 133)
            elif self.shoesSource == ShoesSource.SHOP_WITH_MOONSTONE:
                print("[GameManager] Buy shoes with moonstones")
                self.device.Swipe(924, 591, 924, 118)
                time.sleep(1)
                self.device.Touch(1063, 358)
            else:
                print("[GameManager] Go home")
                self.device.Touch(40, 48)
        elif self.screen.screenType == ScreenType.DIALOG_SHOES_RECHARGE_FP:
            if self.shoesSource == ShoesSource.SHOP_WITH_FP:
                print("[GameManager] Confirm buy shoes with FP")
                self.device.Touch(735, 237)
            else:
                print("[GameManager] Cancel")
                self.device.Touch(735, 477)
        elif self.screen.screenType == ScreenType.DIALOG_SHOES_RECHARGE_II:
            if self.shoesSource == ShoesSource.SHOP_WITH_MOONSTONE:
                print("[GameManager] Confirm buy shoes with moonstones")
                self.device.Touch(735, 237)
            else:
                print("[GameManager] Cancel")
                self.device.Touch(735, 477)
        elif self.screen.screenType == ScreenType.DIALOG_NOT_ENOUGH_FP:
            print("[GameManager] Close dialog. Go to buy shoes by moonstones...")
            self.shoesSource = ShoesSource.SHOP_WITH_MOONSTONE
            self.device.Touch(785, 357)
        else:
            self.GoHome()

    def BuyGoodItemInMagicShop(self):
        screenPiece = self.FindGoodItemInMagicShop()
        if screenPiece is not None:
            print("[GameManager] Open item info")
            self.device.Touch(screenPiece[0] + 193, screenPiece[1] + 70)
        else:
            if self.scrollStep < 2:
                print("[GameManager] No good item is found. Find more...")
                self.device.Swipe(989, 127, 989, 594)
                self.scrollStep = self.scrollStep + 1
            else:
                print("[GameManager] No good item is found")
                self.scrollStep = 0
                self.GoHome()

    def FindGoodItemInMagicShop(self):
        screenPiece = self.screen.Find("Shop_Equipment_Necklace_6stars_Purple.png")
        if screenPiece is not None:
            print("[GameManager] Found 6 stars purple necklace")
            return screenPiece
        screenPiece = self.screen.Find("Shop_Equipment_Ring_6stars_Gold.png")
        if screenPiece is not None:
            print("[GameManager] Found 6 stars gold ring")
            return screenPiece
        return None

    def Summon(self):
        screenPiece = self.screen.Find("Summon_BasicBookAvaiable.png")
        if screenPiece is not None:
            print("[GameManager] Summon basic book")
            self.device.Touch(screenPiece[0] + 127, screenPiece[1] + 88)
            time.sleep(1)
            self.device.Touch(846, 360)
        else:
            screenPiece = self.screen.Find("Summon_MysteriousBookAvaiable.png")
            if screenPiece is not None:
                print("[GameManager] Summon mysterious book")
                self.device.Touch(screenPiece[0] + 127, screenPiece[1] + 88)
                time.sleep(1)
                self.device.Touch(846, 360)
            else:
                self.GoHome()

    def GoHome(self):
        if self.screen.screenType == ScreenType.MAP:
            print("[GameManager] Go home")
            self.device.Touch(1190, 360)
        if self.screen.screenType == ScreenType.PVE_RESULT_VICTORY          \
            or self.screen.screenType == ScreenType.EVENT_DUNGEON_RESULT:
            print("[GameManager] Go home")
            self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Result_Home))
        elif self.screen.screenType == ScreenType.MYSTERIOUS_SANCTUARY      \
            or self.screen.screenType == ScreenType.SHRINE_OF_LIGHT         \
            or self.screen.screenType == ScreenType.GUARDIAN_PLACEMENT      \
            or self.screen.screenType == ScreenType.BATTLE_LIST             \
            or self.screen.screenType == ScreenType.RIVAL_LIST              \
            or self.screen.screenType == ScreenType.BATTLE_RANKING          \
            or self.screen.screenType == ScreenType.BATTLE_DEFENSE_RECORD   \
            or self.screen.screenType == ScreenType.MAIL_BOX_INBOX_TAB      \
            or self.screen.screenType == ScreenType.SHOP                    \
            or self.screen.screenType == ScreenType.SUMMON                  \
            or self.screen.screenType == ScreenType.EVENT_DUNGEON:
            print("[GameManager] Go home")
            self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Back))
        elif self.screen.screenType == ScreenType.DAILY_MISSION_POPUP:
            print("[GameManager] Go to play mission...")
            self.device.Touch(785, 460)
        elif self.screen.screenType == ScreenType.SUMMON_BASIC_DONE         \
            or self.screen.screenType == ScreenType.SUMMON_MYSTEROUS_DONE:
            print("[GameManager] OK")
            self.device.Touch(1185, 361)
        elif self.screen.screenType == ScreenType.LEVEL_UP:
            print("[GameManager] Press anywhere")
            self.device.Touch(500, 500)
        elif self.screen.screenType == ScreenType.SHOP_DIALOG_IS_OPENNING:
            print("[GameManager] Close dialog...")
            self.device.TouchAtPosition(ButtonPositions.GetPosition(Button.Dialog_BuyEquipment_Cancel))
        else:
            print("[GameManager] Idle")

    def AutoTouch(self, autoTime = 2):
        maxTime = autoTime * 60
        interval = 5
        currentTime = 0
        while (currentTime < maxTime):
            tick = time.time()
            self.device.Touch(1200, 425)
            newTick = time.time()
            adbTime = newTick - tick
            sleepTime = interval - adbTime
            if sleepTime < 0:
                currentTime += adbTime
                sleepTime = 0
            else:
                currentTime += interval
            remainingTime = maxTime - currentTime
            print("[GameManager] Auto touch: " + str(remainingTime // 60).zfill(2) + ":" + str(remainingTime % 60).zfill(2))
            time.sleep(sleepTime)