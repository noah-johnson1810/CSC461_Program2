class PackagingStrategy:
    """
    Author: Noah Johnson
    Description: Python conveyor belt project, PackagingStrategy class
    """
    # number of  packages completed
    completedPackages = 0
    # number of boxes per package
    numBoxesPerPackage = -1
    # minimum units to package
    minUnits = -1
    # maximum units to package
    maxUnits = -1
    # packaging type (name of type)
    packagingType = "None"

    def __init__(self, packagingBehavior):
        """
        constructor for packaging strategy, sets the correct strategy based on the parameter
        @param: packagingBehavior: the type of packaging strategy to implement
        @return: true if the station has a box, false otherwise
        """
        self.package = "None"
        self.packagingType = packagingBehavior
        self.stationWaitingArea = list()

        # basic packaging
        if self.packagingType == "Basic":
            # get user input for number of boxes per package
            try:
                self.numBoxesPerPackage = int(input("Number of boxes per package:> "))
                self.package = self.basicPackaging(self.numBoxesPerPackage)
            except:
                raise TypeError
        # restricted packaging
        elif self.packagingType == "Restricted":
            # get user input for the number of boxes, minimum units, and maximum units
            try:
                self.numBoxesPerPackage = int(input("Number of boxes per package:> "))
                self.minUnits = int(input("Minimum Units:> "))
                self.maxUnits = int(input("Maximum Units:> "))
                self.package = self.restrictedPackaging(self.numBoxesPerPackage, self.minUnits, self.maxUnits)
            except:
                raise TypeError
        # preset packaging for test conveyor station 1
        elif self.packagingType == "TestPackaging1":
            self.package = "None"
        # preset packaging for test conveyor station 2
        elif self.packagingType == "TestPackaging2":
            self.numBoxesPerPackage = 2
            self.package = self.basicPackaging(2)
        # preset packaging for test conveyor station 3
        elif self.packagingType == "TestPackaging3":
            self.numBoxesPerPackage = 3
            self.minUnits = 0
            self.maxUnits = 1000
            self.package = self.restrictedPackaging(3, 0, 1000)

    def __repr__(self):
        """
        string representation of this strategy
        @return: a string representation of this strategy
        """
        if self.package == "None":
            return "Packaging: None"
        # initialize empty return string
        returnString = ""
        # add size range for restricted packaging
        if self.packagingType == "Restricted" or self.packagingType == "TestPackaging3":
            returnString += "Size range [" + str(self.minUnits) + ", " + str(self.maxUnits) + "]"
        # append number of boxes per package and unpackaged box ids
        returnString += "\nPackages every " + str(self.numBoxesPerPackage) + \
                        ' boxes \nCurrently has unpackaged box ids:';
        # get box ids
        for box in self.stationWaitingArea:
            returnString += ' ' + str(box.id) + ','
        # remove trailing comma
        returnString = returnString.strip(',')
        # number of completed packages
        returnString += "\nPackages Complete: " + str(self.completedPackages)
        return returnString

    def basicPackaging(self, numBoxesPerPackage):
        """
        the "interface" function (nested, first class) for basic packaging
        @param: numBoxesPerPackage: the number of boxes that make up each package
        @return: the packaging strategy returned as a first class function
        """
        # basic packaging function
        def package(station): # GRADING: BASIC_PACKAGE
            if station.currentBox != '    '\
                and station.currentBox.maxLoad == station.currentBox.units:
                station.waitingArea.append(station.currentBox)
                station.currentBox = '    '
            # if a package is completed
            if len(station.waitingArea) >= int(numBoxesPerPackage):
                self.completedPackages += 1
                station.waitingArea.clear()
        return package

    def restrictedPackaging(self, numBoxesPerPackage, minUnits, maxUnits):
        """
        the "interface" function (nested, first class) for restricted packaging
        @param: numBoxesPerPackage: the number of boxes that make up each package
        @param minUnits: the minimum number of units required to add the box to the package/waiting area
        @param maxUnits: the maximum number of units required to add the box to the package/waiting area
        @return: the packaging strategy returned as a first class function
        """
        # restricted packaging function
        def package(station): # GRADING: RESTRICTED_PACKAGE
            if station.currentBox != '    ' \
                    and int(minUnits) <= station.currentBox.units <= int(maxUnits):
                station.waitingArea.append(station.currentBox)
                station.currentBox = '    '
            # if a package is completed
            if len(station.waitingArea) >= int(numBoxesPerPackage):
                self.completedPackages += 1
                station.waitingArea.clear()
        return package