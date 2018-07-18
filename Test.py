from enum import Enum
from Screen import Screen
from Screen import ScreenType

class TestType(Enum):
    TYPE1 = 0
    TYPE2 = 1
    TYPE3 = 2

class Test:

    def __init__(self):
        self.value = TestType.TYPE1

    def __str__(self):
        return str(self.value)

test = Screen(ScreenType.DEVICE_HOME)
print("Test" + str(test))
