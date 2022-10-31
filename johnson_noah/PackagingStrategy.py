class PackagingStrategy:
    completedPackages = 0
    numBoxesPerPackage = -1
    minUnits = -1
    maxUnits = -1
    packagingType = "None"

    def __init__(self, packagingBehavior):
        self.package = "None"
        self.packagingType = packagingBehavior
        self.stationWaitingArea = list()

        if self.packagingType == "Basic":
            try:
                self.numBoxesPerPackage = int(input("Number of boxes per package:> "))
                self.package = self.basicPackaging(self.numBoxesPerPackage)
            except:
                raise TypeError
        elif self.packagingType == "Restricted":
            try:
                self.numBoxesPerPackage = int(input("Number of boxes per package:> "))
                self.minUnits = int(input("Minimum Units:> "))
                self.maxUnits = int(input("Maximum Units:> "))
                self.package = self.restrictedPackaging(self.numBoxesPerPackage, self.minUnits, self.maxUnits)
            except:
                raise TypeError
        elif self.packagingType == "TestPackaging1":
            self.package = "None"
        elif self.packagingType == "TestPackaging2":
            self.numBoxesPerPackage = 2
            self.package = self.basicPackaging(2)
        elif self.packagingType == "TestPackaging3":
            self.numBoxesPerPackage = 3
            self.minUnits = 0
            self.maxUnits = 1000
            self.package = self.restrictedPackaging(3, 0, 1000)


    def basicPackaging(self, numBoxesPerPackage):
        def package(station):
            if station.currentBox != '    '\
                and station.currentBox.maxLoad == station.currentBox.units:
                station.waitingArea.append(station.currentBox)
                station.currentBox = '    '
            if len(station.waitingArea) >= int(numBoxesPerPackage):
                self.completedPackages += 1
                station.waitingArea.clear()
        return package


    def restrictedPackaging(self, numBoxesPerPackage, minUnits, maxUnits):
        def package(station):
            if station.currentBox != '    ' \
                    and int(minUnits) <= station.currentBox.units <= int(maxUnits):
                station.waitingArea.append(station.currentBox)
                station.currentBox = '    '
            if len(station.waitingArea) >= int(numBoxesPerPackage):
                self.completedPackages += 1
                station.waitingArea.clear()
        return package


    def __repr__(self):
        if self.package == "None":
            return "Packaging: None"

        returnString = ""
        if self.packagingType == "Restricted" or self.packagingType == "TestPackaging3":
            returnString += "Size range [" + str(self.minUnits) + ", " + str(self.maxUnits) + "]"
        returnString += "\nPackages every " + str(self.numBoxesPerPackage) + ' boxes \nCurrently has unpackaged box ids:';
        for box in self.stationWaitingArea:
            returnString += ' ' + str(box.id) + ','
        returnString = returnString.strip(',')
        returnString += "\nPackages Complete: " + str(self.completedPackages)
        return returnString

