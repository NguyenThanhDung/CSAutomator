from enum import Enum

class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Button(Enum):

    Home_Menu = 0
    Home_Guardian = 1
    Home_Battle = 2
    Home_Shop = 3
    Home_Summon = 4

    Shop_MoonstoneShop = 10
    Shop_Moonstones = 11
    Shop_Gold = 12
    Shop_Special = 13
    Shop_MagicShop = 14

class ButtonPositions:

    @staticmethod
    def GetPosition(button):
        
        if button == Button.Home_Menu:
            return Position(1218, 635)
        if button == Button.Home_Guardian:
            return Position(1218, 495)
        if button == Button.Home_Battle:
            return Position(1218, 361)
        if button == Button.Home_Shop:
            return Position(1218, 220)
        if button == Button.Home_Summon:
            return Position(1218, 86)

        if button == Button.Shop_MoonstoneShop:
            return Position(1225, 648)
        if button == Button.Shop_Moonstones:
            return Position(1225, 504)
        if button == Button.Shop_Gold:
            return Position(1225, 360)
        if button == Button.Shop_Special:
            return Position(1225, 213)
        if button == Button.Shop_MagicShop:
            return Position(1225, 73)