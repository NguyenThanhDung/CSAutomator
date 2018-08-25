import os
import time
from Device import Device
from ScreenManager import ScreenManager
from ScreenShot import ScreenShot
from GameManager import GameManager

def Run(isDebugging = False):

    if isDebugging == False:

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

    else:

        device = Device(None)
        device.Connect()
        screenManager = ScreenManager()
        gameManager = GameManager(device)

        print("Debugging...")
        filePath = os.path.abspath("PendingScreens/Shop_MysticalBook_6starsRing.png")
        screenshot = ScreenShot(filePath)

        screen = screenManager.GetScreen(screenshot)
        screen.ShowName()

        gameManager.SetScreen(screen)
        gameManager.Play()

if __name__ == "__main__":
    Run(True)
