from enum import Enum

class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Button(Enum):
    HomeMenu = 0
    HomeGuardian = 1
    HomeBattle = 2
    HomeShop = 3
    HomeSummon = 4

class ButtonPositions:

    @staticmethod
    def GetPosition(button):
        if button == Button.HomeMenu:
            return Position(1218, 635)
        if button == Button.HomeGuardian:
            return Position(1218, 495)
        if button == Button.HomeBattle:
            return Position(1218, 361)
        if button == Button.HomeShop:
            return Position(1218, 220)
        if button == Button.HomeSummon:
            return Position(1218, 86)