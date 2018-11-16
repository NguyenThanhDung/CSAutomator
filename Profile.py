import json
import os
from datetime import datetime
from enum import Enum

class ProfileField(Enum):
    LastDatePlayEventDungeon = 0
    UnknownLandMatchCount = 1

class Profile:

    def __init__(self, accountID):
        self.data = {}
        self.filePath = os.path.abspath("Data/" + accountID + ".json")
        self.Initialize()

    def Initialize(self):
        if os.path.exists(os.path.dirname(self.filePath)) == False:
            os.makedirs(os.path.dirname(self.filePath))
        if os.path.exists(self.filePath) == False:
            today = datetime.now()
            todayString = str(today.year) + "-" + str(today.month) + "-" + str(today.day - 1)
            self.data[ProfileField.LastDatePlayEventDungeon.name] = todayString
            self.data[ProfileField.UnknownLandMatchCount.name] = 0
            with open(self.filePath, 'w') as outfile:
                json.dump(self.data, outfile)

    def Load(self):
        with open(self.filePath) as fileData:
            jsonData = json.load(fileData)
        self.data[ProfileField.LastDatePlayEventDungeon.name] = jsonData[ProfileField.LastDatePlayEventDungeon.name]
        self.data[ProfileField.UnknownLandMatchCount.name] = jsonData[ProfileField.UnknownLandMatchCount.name]

    def Save(self):
        with open(self.filePath, 'w') as outfile:
            json.dump(self.data, outfile)
    
    def GetField(self, fieldID):
        return self.data[fieldID.name]
    
    def SetField(self, fieldID, fieldValue):
        self.data[fieldID.name] = fieldValue

    def DidPlayEventDungeonToday(self):
        dataParts = self.data[ProfileField.LastDatePlayEventDungeon.name].split("-")
        lastDatePlayed = datetime(int(dataParts[0]), int(dataParts[1]), int(dataParts[2]))
        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        return lastDatePlayed == today

    def SaveLastDatePlayEventDungeon(self):
        today = datetime.now()
        todayString = str(today.year) + "-" + str(today.month) + "-" + str(today.day)
        self.data[ProfileField.LastDatePlayEventDungeon.name] = todayString
    
    def DidPlayUnknownLand(self):
        playedCount = self.data[ProfileField.UnknownLandMatchCount.name]
        if playedCount < 10:
            return False
        else:
            return True
    
    def IncreaseUnknownLandMatchCount(self):
        playedCount = self.data[ProfileField.UnknownLandMatchCount.name]
        self.data[ProfileField.UnknownLandMatchCount.name] = playedCount + 1