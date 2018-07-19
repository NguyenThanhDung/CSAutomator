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
        if self.screen.screenType == ScreenType.DAILY_LOGIN_REWARD:
            print("[GameManager] Daily log-in reward")
            self.device.Touch(974, 357)
        if self.screen.screenType == ScreenType.GAME_HOME:
            print("[GameManager] Game home. Open map...")
            self.device.Touch(1174, 360)
        if self.screen.screenType == ScreenType.MAP:
            print("[GameManager] Map. Open Mysterious Sanctuary...")
            self.device.Touch(630, 600)
        if self.screen.screenType == ScreenType.MYSTERIOUS_SANCTUARY:
            print("[GameManager] Mysterious Sanctuary. Open Shrine of Light...")
            self.device.Touch(400, 560)
        else:
            print("[GameManager] Idle")