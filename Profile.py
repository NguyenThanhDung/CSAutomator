import json
import os
from enum import Enum

class ProfileField(Enum):
    DidPlayEventDungeon = 0

class Profile:

    def __init__(self, accountID):
        self.data = {}
        self.filePath = os.path.abspath("Data/" + accountID + ".json")
        self.Initialize()

    def Initialize(self):
        if os.path.exists(os.path.dirname(self.filePath)) == False:
            os.makedirs(os.path.dirname(self.filePath))
        if os.path.exists(self.filePath) == False:
            self.data[ProfileField.DidPlayEventDungeon.name] = False
            with open(self.filePath, 'w') as outfile:
                json.dump(self.data, outfile)

    def Load(self):
        with open(self.filePath) as fileData:
            jsonData = json.load(fileData)
        self.data[ProfileField.DidPlayEventDungeon.name] = jsonData[ProfileField.DidPlayEventDungeon.name]

    def Save(self):
        with open(self.filePath, 'w') as outfile:
            json.dump(self.data, outfile)
    
    def GetField(self, fieldID):
        return self.data[fieldID.name]
    
    def SetField(self, fieldID, fieldValue):
        self.data[fieldID.name] = fieldValue
