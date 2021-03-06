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

    Result_Home = 20
    Result_Guardian = 21
    Result_Map = 22
    Result_Replay = 23
    Result_NextArea = 24

    Dialog_BuyEquipment_Purchase = 30
    Dialog_BuyEquipment_Cancel = 31
    Dialog_BuyEquipment_PurchaseConfirmation_OK = 32
    Dialog_BuyEquipment_PurchaseConfirmation_Cancel = 33

    Back = 999

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

        if button == Button.Result_Home:
            return Position(1200, 663)
        if button == Button.Result_Guardian:
            return Position(1200, 583)
        if button == Button.Result_Map:
            return Position(1200, 503)
        if button == Button.Result_Replay:
            return Position(1200, 336)
        if button == Button.Result_NextArea:
            return Position(1200, 116)
            
        if button == Button.Dialog_BuyEquipment_Purchase:
            return Position(717, 235)
        if button == Button.Dialog_BuyEquipment_Cancel:
            return Position(717, 481)
        if button == Button.Dialog_BuyEquipment_PurchaseConfirmation_OK:
            return Position(783, 244)
        if button == Button.Dialog_BuyEquipment_PurchaseConfirmation_Cancel:
            return Position(783, 472)
            
        if button == Button.Back:
            return Position(40, 48)