from PIL import Image
import pytesseract
from Screen import Screen

class Equipment:

    def __init__(self, screen):
        screenshot = Image.fromarray(screen.image)

        equipmentArea = (385, 106, 763, 614)
        equipmentImage = screenshot.crop(equipmentArea)
        equipmentImage = equipmentImage.rotate(270, expand=1)
        # equipmentImage.show()
        # equipmentImage.save("Temp/Equipment.png")

        mainStatArea = (161, 97, 488, 128)
        mainStatImage = equipmentImage.crop(mainStatArea)
        mainStatText = pytesseract.image_to_string(mainStatImage)
        print("[Equipment] Main Stat: " + mainStatText)

        if "%" not in mainStatText:
            self.isGood = False
        else:
            print("[Equipment] Continue...")