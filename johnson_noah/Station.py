class Station:
    pattern = 'XXXX'

    # box methods

    def getBox(self):
        return self.currentBox

    def setBox(self, newBox):
        self.currentBox = newBox

    def hasBox(self):
        return not self.currentBox == '    '

    def removeBox(self):
        self.currentBox = '    '

    # behavior methods

    def load(self, box):
        if self.__loadBehavior != "None" and self.__loadBehavior.load != "None":
            self.__loadBehavior.load(box)

    def package(self, box):
        if self.__packagingBehavior != "None" and self.__packagingBehavior.package != "None":
            self.__packagingBehavior.package(box)

    def __init__(self, stationNum, loadBehavior="None", packagingBehavior="None"):
        self.stationNum = stationNum
        self.__loadBehavior = loadBehavior
        self.__packagingBehavior = packagingBehavior
        self.currentBox = '    '
        self.waitingArea = list()


    def __str__(self):
        returnString = ""
        currentBox = self.getBox()
        returnString += str(currentBox) + '\n' + str(self.pattern)
        return returnString

    def __repr__(self):
        returnString = "Station " + str(self.stationNum) + "\n"

        if self.hasBox():
            stationHasBox = "True"
        else:
            stationHasBox = "False"
        returnString += "Has box: " + stationHasBox + "\n"

        if self.__packagingBehavior == "None":
            returnString += "Packaging: None\n"
        else:
            self.__packagingBehavior.stationWaitingArea = self.waitingArea
            returnString += repr(self.__packagingBehavior) + "\n"
        return returnString