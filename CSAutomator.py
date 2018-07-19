import time
from Device import Device
from ScreenManager import ScreenManager
from GameManager import GameManager

def Run():
    device = Device("127.0.0.1:62001")
    device.Connect()
    screenManager = ScreenManager()

    while True:
        screenshot = device.CaptureScreen()
        screen = screenManager.GetScreen(screenshot)
        screen.ShowName()

        gameManager = GameManager(device)
        gameManager.SetScreen(screen)
        gameManager.Play()

        time.sleep(5)

if __name__ == "__main__":
    Run()
