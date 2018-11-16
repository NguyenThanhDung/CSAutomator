import cv2
import os

class TemplateImage:

    templateFolder = "ScreenTemplate"

    def __init__(self, screenType, fileName, precision = 100000):
        self.screenType = screenType
        self.criterias = []
        self.AddCriteria(fileName, precision)

    def AddCriteria(self, fileName, precision = 100000):
        filePath = os.path.abspath(TemplateImage.templateFolder + "/" +  fileName)
        self.criterias.append([fileName, cv2.imread(filePath, 0), precision])

    def IsMatch(self, screenShot):
        isFound = True
        for criteria in self.criterias:
            res = cv2.matchTemplate(screenShot.image, criteria[1], cv2.TM_SQDIFF)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            self.Log(str(self.screenType.name).ljust(35) + " " + criteria[0].ljust(50) + " " + str(min_val).rjust(15) + " " + str(min_val < criteria[2]))
            if min_val < criteria[2]:
                continue
            else:
                isFound = False
                break
        return isFound

    def Log(self, log):
        # print("[TemplateImage] " + log)
        return None