import subprocess

class Device:

    def __init__(self, deviceID):
        self.deviceID = ""
        self.screenWidth = 0
        self.screenHeight = 0

    @staticmethod
    def Connect(deviceID):
        print("Device: Connecting to " + deviceID)
        params = ["adb", "connect", deviceID]
        if Device.ExecuteCommand(params):
            print("Device: Connected")
            return Device(deviceID)
        else:
            print("Devece: Fail to connect")
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