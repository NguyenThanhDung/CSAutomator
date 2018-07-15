from Device import Device
from ScreenManager import ScreenManager

SCREENSHOT = "Screenshot.png"

def Run():
    device = Device.Connect("127.0.0.1:62001")
    screenManager = ScreenManager()

    device.CaptureScreen(SCREENSHOT)
    screenManager.Load(SCREENSHOT)
    print(screenManager.IsResultScreen())

if __name__ == "__main__":
    Run()
