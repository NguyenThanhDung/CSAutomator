import json
import os
from datetime import datetime
from enum import Enum

class ProfileField(Enum):
    LastDatePlayEventDungeon = 0
    LastDatePlayUnknownLand = 1
    UnknownLandMatchCount = 2
    LastDatePlayHallOfJudgment = 3

class Profile:

    def __init__(self, accountID):
        self.data = {}
        self.filePath = os.path.abspath("Data/" + accountID + ".json")
        self.Initialize()

    def Initialize(self):
        if os.path.exists(os.path.dirname(self.filePath)) == False:
            os.makedirs(os.path.dirname(self.filePath))
        if os.path.exists(self.filePath) == False:
            yesterdayString = self.GetYesterdayString()
            self.SetField(ProfileField.LastDatePlayEventDungeon, yesterdayString)
            self.SetField(ProfileField.LastDatePlayUnknownLand, yesterdayString)
            self.SetField(ProfileField.UnknownLandMatchCount, 0)
            self.SetField(ProfileField.LastDatePlayHallOfJudgment, yesterdayString)
            with open(self.filePath, 'w') as outfile:
                json.dump(self.data, outfile)

    def Load(self):
        with open(self.filePath) as fileData:
            jsonData = json.load(fileData)
        yesterdayString = self.GetYesterdayString()
        for key in ProfileField:
            if key.name in jsonData:
                self.SetField(key, jsonData[key.name])
            else:
                if key == ProfileField.UnknownLandMatchCount:
                    self.SetField(key, 0)
                else:
                    self.SetField(key, yesterdayString)

    def Save(self):
        with open(self.filePath, 'w') as outfile:
            json.dump(self.data, outfile)
    
    def GetField(self, fieldID):
        return self.data[fieldID.name]
    
    def SetField(self, fieldID, fieldValue):
        self.data[fieldID.name] = fieldValue
    
    def IsToday(self, dateString):
        dateParts = dateString.split("-")
        lastDatePlayed = datetime(int(dateParts[0]), int(dateParts[1]), int(dateParts[2]))
        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        return lastDatePlayed == today

    def GetTodayString(self):
        today = datetime.now()
        return str(today.year) + "-" + str(today.month) + "-" + str(today.day)
    
    def GetYesterdayString(self):
        today = datetime.now()
        return str(today.year) + "-" + str(today.month) + "-" + str(today.day - 1)

    def DidPlayEventDungeonToday(self):
        dateString = self.GetField(ProfileField.LastDatePlayEventDungeon)
        return self.IsToday(dateString)

    def SaveLastDatePlayEventDungeon(self):
        todayString = self.GetTodayString()
        self.SetField(ProfileField.LastDatePlayEventDungeon, todayString)
    
    def DidPlayUnknownLand(self):
        dateString = self.GetField(ProfileField.LastDatePlayUnknownLand)
        if self.IsToday(dateString) == False:
            return False
        playedCount = self.GetField(ProfileField.UnknownLandMatchCount)
        if playedCount < 5:
            return False
        else:
            return True
    
    def IncreaseUnknownLandMatchCount(self):
        dateString = self.GetField(ProfileField.LastDatePlayUnknownLand)
        if self.IsToday(dateString) == False:
            todayString = self.GetTodayString()
            self.SetField(ProfileField.LastDatePlayUnknownLand, todayString)
            self.SetField(ProfileField.UnknownLandMatchCount, 1)
        else:
            playedCount = self.GetField(ProfileField.UnknownLandMatchCount)
            self.SetField(ProfileField.UnknownLandMatchCount, playedCount + 1)
        self.Save()

    def DidPlayHallOfJudgmentToday(self):
        dateString = self.GetField(ProfileField.LastDatePlayHallOfJudgment)
        return self.IsToday(dateString)

    def SaveLastDatePlayHallOfJudgment(self):
        todayString = self.GetTodayString()
        self.SetField(ProfileField.LastDatePlayHallOfJudgment, todayString)