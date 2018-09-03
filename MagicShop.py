class MagicShop:

    def __init__(self):
        self.openedPositions = []

    def DidOpenEquipment(self, position):
        for openedPosition in self.openedPositions:
            if openedPosition.x == position.x and openedPosition.y == position.y:
                return True
        return False

    def AddOpenedEquipment(self, position):
        self.openedPositions.append(position)

    def ClearOpenedEquipments(self):
        del self.openedPositions[:]

    def Log(self, log):
        print("[MagicShop] " + log)
        return None