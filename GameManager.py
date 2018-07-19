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
            print("[GameManager] Tap to start")
            self.device.Touch(self.screen.matchLocation[0], self.screen.matchLocation[1])
        if self.screen.screenType == ScreenType.EVENT_INFO:
            print("[GameManager] Event information")
            self.device.Touch(1215, 630)
            self.device.Touch(1215, 88)
        if self.screen.screenType == ScreenType.DAILY_LOGIN_REWARD:
            print("[GameManager] Daily log-in reward")
            self.device.Touch(974, 357)
        else:
            print("[GameManager] Idle")