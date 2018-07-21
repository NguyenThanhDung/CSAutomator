import time
from Screen import ScreenType

class GameState:
    NONE = 0
    PROMOTION_BATTLE = 1
    MYSTERIOUS_SANCTUARY = 2

class GameManager:

    def __init__(self, device):
        self.device = device
        self.screen = None
        self.gameState = GameState.NONE

    def SetScreen(self, screen):
        self.screen = screen

    def Play(self):
        if self.screen.screenType == ScreenType.DEVICE_HOME:
            print("[GameManager] Start game")
            self.device.Touch(self.screen.matchLocation[0] + 5, self.screen.matchLocation[1] + 5)
            time.sleep(5)
            self.device.LoadDeviceInfo()
        elif self.screen.screenType == ScreenType.TAP_TO_START:
            print("[GameManager] Tap to start...")
            self.device.Touch(self.screen.matchLocation[0], self.screen.matchLocation[1])
        elif self.screen.screenType == ScreenType.EVENT_INFO:
            print("[GameManager] Close event information dialog...")
            self.device.Touch(1215, 630)
        elif self.screen.screenType == ScreenType.DAILY_LOGIN_REWARD:
            print("[GameManager] Close dayly log-gin reward...")
            self.device.Touch(974, 357)
        elif self.screen.screenType == ScreenType.GAME_HOME:
            if self.gameState == GameState.NONE:
                print("[GameManager] Start Promotion Battle...")
                self.gameState = GameState.PROMOTION_BATTLE
                self.PlayPromotionBattle()
            else:
                print("[GameManager] Start Mysterious Sanctuary...")
                self.gameState = GameState.MYSTERIOUS_SANCTUARY
                self.PlayMysteriousSanctuary()
        elif self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_DISABLED:
            print("[GameManager] Enable auto play...")
            self.device.Touch(58, 107)
        else:
            if self.gameState == GameState.NONE:
                self.gameState = GameState.PROMOTION_BATTLE
            if self.gameState == GameState.PROMOTION_BATTLE:
                self.PlayPromotionBattle()
            elif self.gameState == GameState.MYSTERIOUS_SANCTUARY:
                self.PlayMysteriousSanctuary()
    
    def PlayPromotionBattle(self):
        if self.screen.screenType == ScreenType.GAME_HOME:
            print("[GameManager] Open map...")
            self.device.Touch(1174, 360)
        elif self.screen.screenType == ScreenType.MAP:
            print("[GameManager] Open Promotion Battle...")
            self.device.Touch(1077, 547)
        elif self.screen.screenType == ScreenType.MYSTERIOUS_SANCTUARY:
            print("[GameManager] Go home...")
        elif self.screen.screenType == ScreenType.SHRINE_OF_LIGHT:
            print("[GameManager] Go home...")
        elif self.screen.screenType == ScreenType.GUARDIAN_PLACEMENT:
            print("[GameManager] Auto place and start...")
            self.device.Touch(767, 627)
            self.device.Touch(765, 141)
        elif self.screen.screenType == ScreenType.PVE_RESULT_VICTORY:
            print("[GameManager] Go home...")
            #self.AutoTouch(10)
        elif self.screen.screenType == ScreenType.NOT_ENOUGH_SHOES:
            print("[GameManager] Go home...")
            #self.gameState = GameState.PROMOTION_BATTLE
            #self.device.Touch(790, 474)
            #self.device.Touch(1199, 664)
        elif self.screen.screenType == ScreenType.BATTLE_LIST_RIVAL_AVAILABLE:
            print("[GameManager] Open Rival Battle List...")
            self.device.Touch(1221, 505)
        elif self.screen.screenType == ScreenType.RIVAL_LIST_AVAILABLE:
            print("[GameManager] Start Rival match...")
            batteButtonLocaltion = self.screen.Find("PromotionBattle_RivalList_BattleButton.png")
            if batteButtonLocaltion is not None:
                print("[GameManager] Press Battle button at " + str(batteButtonLocaltion))
                self.device.Touch(batteButtonLocaltion[0] + 5, batteButtonLocaltion[1] + 5)
            else:
                print("[GameManager] Schroll down...")
                self.device.Swipe(1116, 351, 569, 349)
        elif self.screen.screenType == ScreenType.RIVAL_MATCH_END:
            print("[GameManager] Press Skip...")
            self.device.Touch(1223, 58)
        elif self.screen.screenType == ScreenType.BATTLE_RESULT:
            print("[GameManager] Press Exit...")
            self.device.Touch(1196, 115)
        else:
            print("[GameManager] Idle")
    
    def PlayMysteriousSanctuary(self):
        if self.screen.screenType == ScreenType.GAME_HOME:
            print("[GameManager] Open map...")
            self.device.Touch(1174, 360)
        elif self.screen.screenType == ScreenType.MAP:
            print("[GameManager] Open Mysterious Sanctuary...")
            self.device.Touch(630, 600)
        elif self.screen.screenType == ScreenType.MYSTERIOUS_SANCTUARY:
            print("[GameManager] Open Shrine of Light...")
            self.device.Touch(400, 560)
        elif self.screen.screenType == ScreenType.SHRINE_OF_LIGHT:
            print("[GameManager] Open floor 6F...")
            self.device.Touch(1115, 120)
        elif self.screen.screenType == ScreenType.GUARDIAN_PLACEMENT:
            print("[GameManager] Auto place and start...")
            self.device.Touch(767, 627)
            self.device.Touch(765, 141)
            self.AutoTouch(10)
        elif self.screen.screenType == ScreenType.PVE_RESULT_VICTORY or self.screen.screenType == ScreenType.ACTION_PHASE_PLAY_ENABLED:
            print("[GameManager] Replay...")
            self.AutoTouch(10)
        elif self.screen.screenType == ScreenType.NOT_ENOUGH_SHOES:
            print("[GameManager] Not enough shoes. Go to battle...")
            self.gameState = GameState.PROMOTION_BATTLE
            self.device.Touch(790, 474)
            self.device.Touch(1199, 664)
        elif self.screen.screenType == ScreenType.BATTLE_LIST_RIVAL_AVAILABLE:
            print("[GameManager] Go home")
            self.device.Touch(38, 46)
        elif self.screen.screenType == ScreenType.RIVAL_LIST_AVAILABLE:
            print("[GameManager] Go home")
            self.device.Touch(38, 46)
        else:
            print("[GameManager] Idle")

    def AutoTouch(self, autoTime):
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