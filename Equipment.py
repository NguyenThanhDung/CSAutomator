from PIL import Image
import pytesseract
from Screen import Screen

class Equipment:

    def __init__(self, screen):
        screenshot = Image.fromarray(screen.image)

        equipmentArea = (385, 106, 763, 614)
        self.equipmentImage = screenshot.crop(equipmentArea)
        self.equipmentImage = self.equipmentImage.rotate(270, expand=1)
        # self.equipmentImage.show()
        # self.equipmentImage.save("Temp/Equipment.png")

        statTexts = {}
        for i in range(5):
            statTexts[i] = self.GetStatText(i)
            print("[Equipment] statText[" + str(i) + "]: " + statTexts[i])

        if "%" not in statTexts[0]:
            self.isGood = False
        else:
            print("[Equipment] Continue...")
            self.isGood = True

    def GetStatText(self, slot):
        if slot == 0:
            return self.ImageToString((385, 97, 488, 128))
        elif slot == 1:
            return self.ImageToString((385, 161, 488, 192))
        if slot == 2:
            return self.ImageToString((385, 192, 488, 221))
        if slot == 3:
            return self.ImageToString((385, 221, 488, 250))
        if slot == 4:
            return self.ImageToString((385, 250, 488, 280))
        else:
            return None
    
    def ImageToString(self, area):
        mainStatImage = self.equipmentImage.crop(area)
        text = pytesseract.image_to_string(mainStatImage)
        text = text.replace("\n", "").replace("\t", "").replace(" ", "")
        return text