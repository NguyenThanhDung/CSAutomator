import subprocess

deviceID = "127.0.0.1:62001"

def ExecuteCommand(params):
    #print("ExecuteCommand: " + ParamToString(params))
    process = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if len(stderr) > 0 :
        print("Device Error: " + stderr)
    else:
        print(stdout)

def Connect():
    params = ["adb", "connect", deviceID]
    ExecuteCommand(params)

def CaptureScreen():
    params = ["adb", "-s", deviceID, "shell", "screencap", "-p", "/sdcard/Screenshot.png"]
    ExecuteCommand(params)

def Pull():
    params = ["adb", "-s", deviceID, "pull", "/sdcard/Screenshot.png"]
    ExecuteCommand(params)

if __name__ == "__main__":
    Connect()
    CaptureScreen()
    Pull()