from Device import Device

def Run():
    device = Device.Connect("127.0.0.1:62001")
    device.CaptureScreen("Screenshot.png")

if __name__ == "__main__":
    Run()
