import math

class LoadStrategy:
    """
    Author: Noah Johnson
    Description: Python conveyor belt project, LoadStrategy class
    """

    def __init__(self, loadBehavior):
        """
        constructor for the loadStrategy, sets the appropriate strategy based on the parameter
        @param: loadBehavior: determines what type of strategy to implement
        @return: none
        """
        self.loadType = loadBehavior
        self.load = "None"

        # basic loading
        if self.loadType == "Basic":
            numUnits = input("Number of units:> ")
            self.load = self.basicLoad(numUnits)
        # percentage loading
        elif self.loadType == "Percentage":
            try:
                percentage = input("Percentage of box:> ")
                percentage = int(percentage)
            except:
                raise TypeError
            self.load = self.percentageLoad(percentage)
        # preset strategy for the test conveyor, station 1
        elif self.loadType == "TestLoading1":
            self.load = "None"
        # preset strategy for the test conveyor, station 2
        elif self.loadType == "TestLoading2":
            self.load = self.basicLoad(2)
        # preset strategy for the test conveyor, station 3
        elif self.loadType == "TestLoading3":
            self.load = self.percentageLoad(50)


    def basicLoad(self, numUnits):
        """
        the basic load "interface" function
        @param: numUnits: the number of units to try to load into each box
        @return: the function which performs the basic load strategy
        """
        # first class nested load function
        def load(box): # GRADING: BASIC_LOAD
            box.units = int(numUnits) + box.units if int(numUnits) + box.units < box.maxLoad else box.maxLoad
            return box
        return load

    def percentageLoad(self, percentage):
        """
        the percentage load "interface" function
        @param: percentage: the percentage of the maximum units to try to load into each box
        @return: the function which performs the percentage load strategy
        """
        def load(box): # GRADING: PERCENT_LOAD
            box.units = math.floor(box.maxLoad * (int(percentage) / 100)) + box.units if math.floor(box.maxLoad * (int(percentage) / 100)) + box.units < box.maxLoad else int(box.maxLoad)
            return box
        return load


