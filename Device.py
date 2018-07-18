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
            if "SurfaceOrientation" in line:
                orientationLine = line.split(' ')
                orientation = orientationLine[len(orientationLine)-1]
                if orientation == 0 or orientation == 2:
                    self.screenOrientation = ScreenOrientation.LANDSCAPE
                else:
                    self.screenOrientation = ScreenOrientation.PORTRAIT
                break
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
        print("[Device " + self.deviceID + "] Touch " + str(x) + " " + str(y))
        params = ["adb", "-s", self.deviceID, "shell", "input", "tap", str(x), str(y)]
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