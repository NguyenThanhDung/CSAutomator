from enum import Enum

class GameState(Enum):
    NONE = 0
    DAILY_MISSION = 1
    PROMOTION_BATTLE = 2
    MYSTERIOUS_SANCTUARY = 3
    OUT_OF_SHOES = 4
    SHOPPING = 5
    SUMMON = 6

class ShoesSource(Enum):
    DAILY_MISSION_REWARD = 0
    MAIL_BOX = 1
    SHOP_WITH_FP = 2
    SHOP_WITH_MOONSTONE = 3

class DailyMission(Enum):
    NONE = 0
    POWER_UP_GUARDIAN = 1
    SUMMON_GUARDIAN = 2
    POWER_UP_EQUIPMENT = 3
    DISASSEMBLY = 4
    DEAR_FRIEND = 5

class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y