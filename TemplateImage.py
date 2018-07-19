import cv2
import os

class TemplateImage:

    templateFolder = "ScreenTemplate"

    def __init__(self, screenType, fileName, precision = 1000000):
        self.screenType = screenType
        self.criterias = []
        self.AddCriteria(fileName, precision)

    def AddCriteria(self, fileName, precision = 1000000):
        filePath = os.path.abspath(TemplateImage.templateFolder + "/" +  fileName)
        self.criterias.append([fileName, cv2.imread(filePath, 0), precision])

    def FindMatch(self, screenShot):
        result = FindMatchResult(True, [0, 0])
        for criteria in self.criterias:
            res = cv2.matchTemplate(screenShot.image, criteria[1], cv2.TM_SQDIFF)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            print("[ScreenManager] IsMatch() " + str(self.screenType).ljust(30) + " " + criteria[0].ljust(40) + " " + str(min_val).rjust(15) + " " + str(min_val < criteria[2]))
            if min_val < criteria[2]:
                result.location = min_loc
            else:
                result.isMatch = False
                break
        return result

class FindMatchResult:

    def __init__(self, isMatch, location):
        self.isMatch = isMatch
        self.location = location