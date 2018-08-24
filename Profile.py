import json
import os

class Profile:

    def __init__(self, accountID):
        self.filePath = os.path.abspath("Data/" + accountID + ".json")

    def Load(self):
        try:
            with open(self.filePath) as fileData:
                jsonData = json.load(fileData)
            self.didPlayEventDungeon = jsonData["didPlayEventDungeon"]
        except IOError:
            self.SaveDefault()

    def Save(self):
        print("Save " + self.filePath)

    def SaveDefault(self):
        data = {}
        data["didPlayEventDungeon"] = False
        if os.path.exists(os.path.dirname(self.filePath)) == False:
            os.makedirs(os.path.dirname(self.filePath))
        with open(self.filePath, 'w') as outfile:  
            json.dump(data, outfile)