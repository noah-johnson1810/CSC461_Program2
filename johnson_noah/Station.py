class Station:
    """
    Author: Noah Johnson
    Description: Python Conveyor Belt project, Station class
    """
    pattern = 'XXXX'

    def __init__(self, stationNum, loadBehavior="None", packagingBehavior="None"):
        """
        constructor for Station, sets the stationNum, loadBehavior, and packagingBehavior
        @type stationNum: number
        @param stationNum: the station number for this station
        @type loadBehavior: String
        @param loadBehavior: the loading behavior for this station
        @type packagingBehavior: String
        @param packagingBehavior: the packaging behavior for this station
        @return: none
        """
        self.stationNum = stationNum
        self.__loadBehavior = loadBehavior
        self.__packagingBehavior = packagingBehavior
        self.currentBox = '    '
        self.waitingArea = list()

    def __repr__(self):
        """
        generates the string representation for this Station
        @return: the string representation for this Station
        """
        returnString = "Station " + str(self.stationNum) + "\n"
        # check if station has a box
        if self.hasBox():
            stationHasBox = "True"
        else:
            stationHasBox = "False"
        returnString += "Has box: " + stationHasBox + "\n"
        # check packaging behavior
        if self.__packagingBehavior == "None":
            returnString += "Packaging: None\n"
        else:
            self.__packagingBehavior.stationWaitingArea = self.waitingArea
            returnString += repr(self.__packagingBehavior) + "\n"
        return returnString

    def __str__(self):
        """
        generates the toString (str()) for this Station
        @return: the string containing the str() information
        """
        returnString = ""
        currentBox = self.getBox()
        returnString += str(currentBox) + '\n' + str(self.pattern)
        return returnString

    def getBox(self):
        """
        gets the box currently in the station
        @return: the box currently in the station
        """
        return self.currentBox

    def hasBox(self):
        """
        determines whether the Station currently has a box
        @return: true if the station has a box, false otherwise
        """
        return not self.currentBox == '    '

    def load(self, box):
        """
        performs a load (by calling the load function, this method doesn't know what the behavior is)
        @param box: the box to load
        @return: none
        """
        if self.__loadBehavior != "None" and self.__loadBehavior.load != "None":
            self.__loadBehavior.load(box)

    def package(self, box):
        """
         performs packaging (by calling the package function, doesn't know what the behavior is)
        @param box: the box to perform packaging on
        @return: none
        """
        if self.__packagingBehavior != "None" and self.__packagingBehavior.package != "None":
            self.__packagingBehavior.package(box)

    def removeBox(self):
        """
        removes the current box from the station
        @return: none
        """
        self.currentBox = '    '

    def setBox(self, newBox):
        """
        sets the current box of the station to the box passed in
        @param newBox: the new box to set the current box of the station to
        @return: none
        """
        self.currentBox = newBox