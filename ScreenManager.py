import cv2

class ScreenManager:

    def __init__(self):
        self.threadHold = 1000
        self.resultScreenTemplate = cv2.imread("ScreenTemplate\Result.png", 0)

    def Load(self, fileName):
        self.screen = cv2.imread(fileName, 0)

    def IsResultScreen(self):
        res = cv2.matchTemplate(self.screen, self.resultScreenTemplate, cv2.TM_SQDIFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print("[ScreenManager] Compare value: " + str(min_val))
        if min_val < self.threadHold:
            return True
        else:
            return False