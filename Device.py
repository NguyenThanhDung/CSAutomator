import subprocess
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
        if Device.ExecuteCommand(params):
            print("[Device " + self.deviceID + "] Connected")
            self.GetDeviceInfo()
            return True
        else:
            print("[Device " + self.deviceID + "] Fail to connect")
            return False

    def GetDeviceInfo(self):
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
                orientation = orientationLine[len(orientationLine)-1]
                if orientation == 0 or orientation == 2:
                    self.screenOrientation = ScreenOrientation.LANDSCAPE
                else:
                    self.screenOrientation = ScreenOrientation.PORTRAIT
                continue
        print("[Device " + self.deviceID + "] Screen size: " + str(self.screenWidth) + " " + str(self.screenHeight))
        print("[Device " + self.deviceID + "] " + str(self.screenOrientation))

    def CaptureScreen(self):
        params = ["adb", "-s", self.deviceID, "shell", "screencap", "-p", "/sdcard/" + Device.screenShotFileName]
        if Device.ExecuteCommand(params) is None:
            return
        self.Pull(Device.screenShotFileName)
        return ScreenShot(Device.screenShotFileName)

    
    def Pull(self, fileName):
        params = ["adb", "-s", self.deviceID, "pull", "/sdcard/" + fileName]
        Device.ExecuteCommand(params)

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

    @staticmethod
    def ExecuteCommand(params):
        #print("ExecuteCommand: " + ParamToString(params))
        process = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if len(stderr) > 0 :
            print("Device Error: " + stderr)
            return None
        return stdout