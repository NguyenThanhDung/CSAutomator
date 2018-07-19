import time
from Screen import ScreenType

class GameManager:

    def __init__(self, device):
        self.device = device
        self.screen = None

    def SetScreen(self, screen):
        self.screen = screen
    
    def Play(self):
        if self.screen.screenType == ScreenType.DEVICE_HOME:
            print("[GameManager] Start game")
            self.device.Touch(self.screen.matchLocation[0] + 5, self.screen.matchLocation[1] + 5)
            time.sleep(5)
            self.device.LoadDeviceInfo()
        if self.screen.screenType == ScreenType.TAP_TO_START:
            print("[GameManager] Tap to start...")
            self.device.Touch(self.screen.matchLocation[0], self.screen.matchLocation[1])
        if self.screen.screenType == ScreenType.EVENT_INFO:
            print("[GameManager] Close event information dialog...")
            self.device.Touch(1215, 630)
        if self.screen.screenType == ScreenType.DAILY_LOGIN_REWARD:
            print("[GameManager] Close dayly log-gin reward...")
            self.device.Touch(974, 357)
        if self.screen.screenType == ScreenType.GAME_HOME:
            print("[GameManager] Open map...")
            self.device.Touch(1174, 360)
        if self.screen.screenType == ScreenType.MAP:
            print("[GameManager] Open Mysterious Sanctuary...")
            self.device.Touch(630, 600)
        if self.screen.screenType == ScreenType.MYSTERIOUS_SANCTUARY:
            print("[GameManager] Open Shrine of Light...")
            self.device.Touch(400, 560)
        if self.screen.screenType == ScreenType.SHRINE_OF_LIGHT:
            print("[GameManager] Open floor 6F...")
            self.device.Touch(1115, 120)
        if self.screen.screenType == ScreenType.GUARDIAN_PLACEMENT:
            print("[GameManager] Auto place and start...")
            self.device.Touch(767, 627)
            self.device.Touch(765, 141)
            self.AutoTouch(10)
        if self.screen.screenType == ScreenType.PVE_RESULT_VICTORY or self.screen.screenType == ScreenType.ACTION_PHASE:
            print("[GameManager] Replay...")
            self.AutoTouch(10)
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