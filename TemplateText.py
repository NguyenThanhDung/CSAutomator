from PIL import Image
import pytesseract

class TemplateText:
    
    def __init__(self, screenType, text, x, y, w, h):
        self.screenType = screenType
        self.text = text
        self.analyzedArea = (x, y, x + w, y + h)
    
    def IsMatch(self, screenShot):
        screenshotImage = Image.fromarray(screenShot.image)
        screenshotImage = screenshotImage.crop(self.analyzedArea)
        screenshotImage = screenshotImage.rotate(270, expand=1)
        text = pytesseract.image_to_string(screenshotImage)
        self.Log("Text:" + text)
        return text == self.text
    
    def Log(self, log):
        print("[TemplateText] " + log)
        return None