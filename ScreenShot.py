import cv2

class ScreenShot:

    def __init__(self, fileName):
        self.fileName = fileName
        self.image = cv2.imread(fileName, 0)
