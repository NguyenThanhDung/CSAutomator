import subprocess
import sys
from enum import Enum
from ScreenShot import ScreenShot

class ScreenOrientation(Enum):
    LANDSCAPE = 0
    PORTRAIT = 1

class Device:

    screenShotFileName = "Screenshot.png"

    def __init__(self, deviceID):
        self.deviceID = deviceID
        self.screenWidth = 0
        self.screenHeight = 0
        self.screenOrientation = 0

    def Connect(self):
        print("[Device " + self.deviceID + "] Connecting...")
        params = ["adb", "connect", self.deviceID]
        Device.ExecuteCommand(params)
        print("[Device " + self.deviceID + "] Connected")
        self.LoadDeviceInfo()

    def LoadDeviceInfo(self):
        params = ["adb", "-s", self.deviceID, "shell", "dumpsys", "input"]
        info = Device.ExecuteCommand(params)
        if info is None:
            return
        lines = info.split('\n')
        for line in lines:
            if "SurfaceWidth" in line:
                widthLine = line.split(' ')
                self.screenWidth = int(widthLine[len(widthLine)-1][:-4])
                continue
            elif "SurfaceHeight" in line:
                heightLine = line.split(' ')
                self.screenHeight = int(heightLine[len(heightLine)-1][:-4])
                continue
            elif "SurfaceOrientation" in line:
                orientationLine = line.split(' ')
                orientation = int(orientationLine[len(orientationLine)-1])
                if orientation == 0 or orientation == 2:
                    self.screenOrientation = ScreenOrientation.LANDSCAPE
                else:
                    self.screenOrientation = ScreenOrientation.PORTRAIT
                continue
        print("[Device " + self.deviceID + "] Screen size: " + str(self.screenWidth) + " " + str(self.screenHeight))
        print("[Device " + self.deviceID + "] " + str(self.screenOrientation))

    def CaptureScreen(self):
        params = ["adb", "-s", self.deviceID, "shell", "screencap", "-p", "/sdcard/" + Device.screenShotFileName]
        Device.ExecuteCommand(params)
        self.Pull(Device.screenShotFileName)
        return ScreenShot(Device.screenShotFileName)

    
    def Pull(self, fileName):
        params = ["adb", "-s", self.deviceID, "pull", "/sdcard/" + fileName]
        Device.ExecuteCommand(params)

    def TouchAtPosition(self, position):
        self.Touch(position.x, position.y)

    def Touch(self, x, y):
        if self.screenOrientation == ScreenOrientation.LANDSCAPE:
            touchX = x
            touchY = y
        else:
            touchX = self.screenHeight - y
            touchY = x
        print("[Device " + self.deviceID + "] Touch " + str(touchX) + " " + str(touchY))
        params = ["adb", "-s", self.deviceID, "shell", "input", "tap", str(touchX), str(touchY)]
        Device.ExecuteCommand(params)

    def Swipe(self, beginX, beginY, endX, endY, duration = 500):
        if self.screenOrientation == ScreenOrientation.LANDSCAPE:
            touchBeginX = beginX
            touchBeginY = beginY
            touchEndX = endX
            touchEndY = endY
        else:
            touchBeginX = self.screenHeight - beginY
            touchBeginY = beginX
            touchEndX = self.screenHeight - endY
            touchEndY = endX
        print("[Device " + self.deviceID + "] Swipe " + str(touchBeginX) + ":" + str(touchBeginY) + " to " + str(touchEndX) + ":" + str(touchEndY))
        params = ["adb", "-s", self.deviceID, "shell", "input", "swipe", str(touchBeginX), str(touchBeginY), str(touchEndX), str(touchEndY), str(duration)]
        Device.ExecuteCommand(params)

    @staticmethod
    def ExecuteCommand(params):
        # print("[Popen] ExecuteCommand: " + ParamToString(params))
        try:
            process = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            # print("[Popen] Return Code: " + str(process.returncode))
            # if output:
            #     print("[Popen] Output: " + output)
            if error:
                print("[Popen] Error: " + error)
            if output:
                return output
        except OSError as e:
            print("[Popen] OSError: " + e.errno)
            print("[Popen] OSError: " + e.strerror)
            print("[Popen] OSError: " + e.filename)
        except:
            print("[Popen] SysError: " + sys.exc_info()[0])