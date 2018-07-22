import time
from enum import Enum
from Screen import ScreenType

class GameState(Enum):
    NONE = 0
    PROMOTION_BATTLE = 1
    MYSTERIOUS_SANCTUARY = 2
    OUT_OF_SHOES = 3

class ScrollDirection(Enum):
    UP = 0
    DOWN = 1

class ShoesSource(Enum):
    DAILY_MISSION_REWARD = 0
    MAIL_BOX = 1
    SHOP = 2

class GameManager:

    def __init__(self, device):
        self.device = device
        self.screen = None
        self.gameState = GameState.NONE
        self.scrollDirection = ScrollDirection.UP
        self.scrollStep = 0
        self.shoesSource = ShoesSource.DAILY_MISSION_REWARD

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
            print("[GameManager] Close event information dialog...")
            self.device.Touch(1215, 630)
        elif self.screen.screenType == ScreenType.DAILY_LOGIN_REWARD:
            print("[GameManager] Close dayly log-gin reward...")
            self.device.Touch(974, 357)
        elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_DISABLED:
            print("[GameManager] Enable auto play")
            self.device.Touch(58, 107)
        elif self.screen.screenType == ScreenType.REWARD_INFO:
            print("[GameManager] Press OK")
            self.device.Touch(797, 356)
        elif self.screen.screenType == ScreenType.NOT_ENOUGH_TICKETS:
            print("[GameManager] Go to Mysterious Sanctuary...")
            self.gameState = GameState.MYSTERIOUS_SANCTUARY
            self.device.Touch(788, 471)
            self.device.Touch(40, 48)
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
                    print("[GameManager] Collected all rewards, go to Mysterious Sanctuary")
                    self.gameState = GameState.PROMOTION_BATTLE
                    self.shoesSource == ShoesSource.MAIL_BOX
                    self.device.Touch(40, 48)
        else:
            if self.gameState == GameState.NONE:
                self.gameState = GameState.PROMOTION_BATTLE
            if self.gameState == GameState.PROMOTION_BATTLE:
                self.PlayPromotionBattle()
            elif self.gameState == GameState.MYSTERIOUS_SANCTUARY:
                self.PlayMysteriousSanctuary()
            elif self.gameState == GameState.OUT_OF_SHOES:
                self.FindShoes()
    
    def PlayPromotionBattle(self):
        if self.screen.screenType == ScreenType.GAME_HOME:
            print("[GameManager] Open map")
            self.device.Touch(1174, 360)
        elif self.screen.screenType == ScreenType.MAP:
            print("[GameManager] Open Promotion Battle")
            self.device.Touch(1077, 547)
        elif self.screen.screenType == ScreenType.MYSTERIOUS_SANCTUARY:
            print("[GameManager] Go home")
            self.device.Touch(40, 48)
        elif self.screen.screenType == ScreenType.SHRINE_OF_LIGHT:
            print("[GameManager] Go home")
            self.device.Touch(40, 48)
        elif self.screen.screenType == ScreenType.GUARDIAN_PLACEMENT:
            print("[GameManager] Auto place and start")
            self.device.Touch(767, 627)
            self.device.Touch(765, 141)
        elif self.screen.screenType == ScreenType.PVE_RESULT_VICTORY:
            print("[GameManager] Go home")
            self.device.Touch(1199, 664)
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
                    self.device.Touch(potentialMatch[0] + 40, potentialMatch[1] + 70)
                else:
                    if self.scrollDirection == ScrollDirection.UP:
                        if self.scrollStep < 2:
                            print("[GameManager] Can not find any potential match, scroll up")
                            self.device.Swipe(1116, 226, 569, 226)
                            self.scrollStep = self.scrollStep + 1
                        else:
                            self.scrollDirection = ScrollDirection.DOWN
                            self.scrollStep = 0
                            refreshAvailable = self.screen.Find("PromotionBattle_BattleList_RefreshAvailable.png")
                            if refreshAvailable is not None:
                                print("[GameManager] There isn't any potential match, refresh list")
                                self.device.Touch(514, 108)
                            else:
                                print("[GameManager] There isn't any potential match, refresh is not available, go to Mysterious Sanctuary")
                                self.gameState = GameState.MYSTERIOUS_SANCTUARY
                    else:
                        if self.scrollStep < 2:
                            print("[GameManager] Can not find any potential match, scroll down")
                            self.device.Swipe(569, 226, 1116, 226)
                            self.scrollStep = self.scrollStep + 1
                        else:
                            self.scrollDirection = ScrollDirection.UP
                            self.scrollStep = 0
                            refreshAvailable = self.screen.Find("PromotionBattle_BattleList_RefreshAvailable.png")
                            if refreshAvailable is not None:
                                print("[GameManager] There isn't any potential match, refresh list")
                                self.device.Touch(514, 108)
                            else:
                                print("[GameManager] There isn't any potential match, refresh is not available, go to Mysterious Sanctuary")
                                self.gameState = GameState.MYSTERIOUS_SANCTUARY
        elif self.screen.screenType == ScreenType.BATTLE_LIST_REFRESH_CONFIRMATION:
            print("[GameManager] Confirm refresh")
            self.device.Touch(784, 243)
        elif self.screen.screenType == ScreenType.BATTLE_LIST_REFRESH_WITH_MOONSTONE:
            print("[GameManager] Don't refresh with moonstone")
            self.device.Touch(784, 474)
        elif self.screen.screenType == ScreenType.RIVAL_LIST:
            revalAvailable = self.screen.Find("PromotionBattle_RivalList_Available.png")
            if revalAvailable is not None:
                print("[GameManager] Start Rival match...")
                batteButtonLocaltion = self.screen.Find("PromotionBattle_RivalList_BattleButton.png")
                if batteButtonLocaltion is not None:
                    print("[GameManager] Press Battle button at " + str(batteButtonLocaltion))
                    self.device.Touch(batteButtonLocaltion[0] + 5, batteButtonLocaltion[1] + 5)
                else:
                    print("[GameManager] Schroll down")
                    self.device.Swipe(1116, 351, 569, 351)
            else:
                print("[GameManager] Switch to Battle list")
                self.device.Touch(1218, 646)
        elif self.screen.screenType == ScreenType.RIVAL_MATCH_END:
            print("[GameManager] Press Skip")
            self.device.Touch(1223, 58)
        elif self.screen.screenType == ScreenType.BATTLE_RESULT:
            print("[GameManager] Press Exit")
            self.device.Touch(1196, 115)
        else:
            print("[GameManager] Idle")
    
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
            print("[GameManager] Open floor 6F")
            self.device.Touch(1115, 120)
        elif self.screen.screenType == ScreenType.GUARDIAN_PLACEMENT:
            print("[GameManager] Auto place and start")
            self.device.Touch(767, 627)
            self.device.Touch(765, 141)
        elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_ENABLED:
            print("[GameManager] Replay...")
            self.AutoTouch()
        elif self.screen.screenType == ScreenType.PVE_RESULT_VICTORY:
            print("[GameManager] Go to battle")
            self.gameState = GameState.PROMOTION_BATTLE
            self.device.Touch(1199, 664)
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
            print("[GameManager] Go home")
            self.device.Touch(38, 46)
        elif self.screen.screenType == ScreenType.BATTLE_LIST_REFRESH_CONFIRMATION:
            print("[GameManager] Confirm refresh")
            self.device.Touch(784, 243)
        elif self.screen.screenType == ScreenType.BATTLE_LIST_REFRESH_WITH_MOONSTONE:
            print("[GameManager] Don't refresh with moonstone")
            self.device.Touch(784, 474)
        elif self.screen.screenType == ScreenType.RIVAL_LIST:
            print("[GameManager] Go home")
            self.device.Touch(38, 46)
        elif self.screen.screenType == ScreenType.RIVAL_MATCH_END:
            print("[GameManager] Press Skip...")
            self.device.Touch(1223, 58)
        elif self.screen.screenType == ScreenType.BATTLE_RESULT:
            print("[GameManager] Press Exit...")
            self.device.Touch(1196, 115)
        else:
            print("[GameManager] Idle")

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
            elif self.shoesSource == ShoesSource.SHOP:
                print("[GameManager] Open shop")
        elif self.screen.screenType == ScreenType.MAP:
            print("[GameManager] Go home")
            self.device.Touch(1190, 360)
        elif self.screen.screenType == ScreenType.MYSTERIOUS_SANCTUARY:
            print("[GameManager] Go home")
            self.device.Touch(40, 48)
        elif self.screen.screenType == ScreenType.SHRINE_OF_LIGHT:
            print("[GameManager] Go home")
            self.device.Touch(40, 48)
        elif self.screen.screenType == ScreenType.GUARDIAN_PLACEMENT:
            print("[GameManager] Go home")
            self.device.Touch(40, 48)
        #elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_ENABLED:
        elif self.screen.screenType == ScreenType.PVE_RESULT_VICTORY:
            print("[GameManager] Go home")
            self.device.Touch(1197, 663)
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
            print("[GameManager] Go home")
            self.device.Touch(38, 46)
        elif self.screen.screenType == ScreenType.BATTLE_LIST_REFRESH_CONFIRMATION:
            print("[GameManager] Confirm refresh")
            self.device.Touch(784, 243)
        elif self.screen.screenType == ScreenType.BATTLE_LIST_REFRESH_WITH_MOONSTONE:
            print("[GameManager] Don't refresh with moonstone")
            self.device.Touch(784, 474)
        elif self.screen.screenType == ScreenType.RIVAL_LIST:
            print("[GameManager] Go home")
            self.device.Touch(38, 46)
        elif self.screen.screenType == ScreenType.RIVAL_MATCH_END:
            print("[GameManager] Press Skip...")
            self.device.Touch(1223, 58)
        elif self.screen.screenType == ScreenType.BATTLE_RESULT:
            print("[GameManager] Press Exit...")
            self.device.Touch(1196, 115)
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