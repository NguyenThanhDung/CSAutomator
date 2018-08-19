import time
from Device import Device
from ScreenManager import ScreenManager
from GameManager import GameManager

def Run():
    device = Device("127.0.0.1:62001")
    device.Connect()
    screenManager = ScreenManager()
    gameManager = GameManager(device)

    while True:
        screenshot = device.CaptureScreen()
        if screenshot.image is None:
            print("Can not capture screenshot. Retry...")
            time.sleep(5)
            continue

        screen = screenManager.GetScreen(screenshot)
        screen.ShowName()

        gameManager.SetScreen(screen)
        gameManager.Play()

        print("")
        time.sleep(5)

if __name__ == "__main__":
    Run()
