from Device import Device
from ScreenManager import ScreenManager

def Run():
    device = Device("127.0.0.1:62001")
    device.Connect()
    screenManager = ScreenManager()

    screenshot = device.CaptureScreen()
    screen = screenManager.GetScreen(screenshot)
    print("Screen: " + str(screen))

if __name__ == "__main__":
    Run()
