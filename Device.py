import subprocess
from ScreenShot import ScreenShot

class Device:

    screenShotFileName = "Screenshot.png"

    def __init__(self, deviceID):
        self.deviceID = deviceID

    def Connect(self):
        print("[Device " + self.deviceID + "] Connecting...")
        params = ["adb", "connect", self.deviceID]
        if Device.ExecuteCommand(params):
            print("[Device " + self.deviceID + "] Connected")
            return True
        else:
            print("[Device " + self.deviceID + "] Fail to connect")
            return False

    def CaptureScreen(self):
        params = ["adb", "-s", self.deviceID, "shell", "screencap", "-p", "/sdcard/" + Device.screenShotFileName]
        if Device.ExecuteCommand(params) == False:
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
            return False
        return True