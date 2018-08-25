import json
import os

class Profile:

    def __init__(self, accountID):
        self.filePath = os.path.abspath("Data/" + accountID + ".json")
        self.Initialize()

    def Initialize(self):
        if os.path.exists(os.path.dirname(self.filePath)) == False:
            os.makedirs(os.path.dirname(self.filePath))
        if os.path.exists(self.filePath) == False:
            data = {}
            data["didPlayEventDungeon"] = False
            with open(self.filePath, 'w') as outfile:
                json.dump(data, outfile)

    def Load(self):
        with open(self.filePath) as fileData:
            jsonData = json.load(fileData)
        self.didPlayEventDungeon = jsonData["didPlayEventDungeon"]

    def Save(self):
        data = {}
        data["didPlayEventDungeon"] = self.didPlayEventDungeon
        with open(self.filePath, 'w') as outfile:
            json.dump(data, outfile)
