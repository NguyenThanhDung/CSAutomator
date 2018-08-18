# pip install pytesseract
# https://github.com/UB-Mannheim/tesseract/wiki

import os
from PIL import Image
import pytesseract

fileName = "EquipmentScreen.png"
filePath = os.path.abspath("Test/" + fileName)
image = Image.open(filePath)

equipmentArea = (91, 347, 471, 713)
equipmentImage = image.crop(equipmentArea)
equipmentImage = equipmentImage.rotate(270, expand=1)
equipmentFilePath = os.path.abspath("Test/Equipment.png")
equipmentImage.save(equipmentFilePath)

# mainStatArea = (178, 371, 212, 558)
# mainStatImage = image.crop(mainStatArea)
# # mainStatImage.show()
# text = pytesseract.image_to_string(mainStatImage)
# print(text)

# X: 91
# Y: 347
# W: 380
# H: 366
# print(str(347 + 366))