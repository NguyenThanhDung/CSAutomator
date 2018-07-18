from Screen import ScreenType
#from Device import Device

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
        if self.screen.screenType == ScreenType.TAP_TO_START:
            print("[GameManager] Tap to start")
            self.device.Touch(self.screen.matchLocation[0], self.screen.matchLocation[1])
        else:
            print("[GameManager] Idle")