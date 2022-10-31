import math

class LoadStrategy:
    def __init__(self, loadBehavior):

        self.loadType = loadBehavior
        self.load = "None"

        if self.loadType == "Basic":
            numUnits = input("Number of units:> ")
            self.load = self.basicLoad(numUnits)
        elif self.loadType == "Percentage":
            try:
                percentage = input("Percentage of box:> ")
                percentage = int(percentage)
            except:
                raise TypeError
            self.load = self.percentageLoad(percentage)
        elif self.loadType == "TestLoading1":
            self.load = "None"
        elif self.loadType == "TestLoading2":
            self.load = self.basicLoad(2)
        elif self.loadType == "TestLoading3":
            self.load = self.percentageLoad(50)



    def basicLoad(self, numUnits):
        def load(box):
            box.units = int(numUnits) + box.units if int(numUnits) + box.units < box.maxLoad else box.maxLoad
            return box
        return load

    def percentageLoad(self, percentage):
        def load(box):
            box.units = math.floor(box.maxLoad * (int(percentage) / 100)) + box.units if math.floor(box.maxLoad * (int(percentage) / 100)) + box.units < box.maxLoad else int(box.maxLoad)
            return box
        return load


