import subprocess

class Device:

    def __init__(self, deviceID):
        self.deviceID = deviceID
        self.screenWidth = 0
        self.screenHeight = 0

    def CaptureScreen(self, fileName):
        params = ["adb", "-s", self.deviceID, "shell", "screencap", "-p", "/sdcard/" + fileName]
        if Device.ExecuteCommand(params) == False:
            return
        self.Pull(fileName)

    
    def Pull(self, fileName):
        params = ["adb", "-s", self.deviceID, "pull", "/sdcard/" + fileName]
        Device.ExecuteCommand(params)

    @staticmethod
    def Connect(deviceID):
        print("Device: Connecting to " + deviceID)
        params = ["adb", "connect", deviceID]
        if Device.ExecuteCommand(params):
            print("Device: Connected")
            return Device(deviceID)
        else:
            print("Device: Fail to connect")
            return None

    @staticmethod
    def ExecuteCommand(params):
        #print("ExecuteCommand: " + ParamToString(params))
        process = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if len(stderr) > 0 :
            print("Device Error: " + stderr)
            return False
        return True