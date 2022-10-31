from johnson_noah.Station import Station
from johnson_noah.StationIterator import StationIterator

class Conveyor:
    currentID = 1

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        try:
            self.__index += 1
            return self.layout[self.__index]
        except:
            raise StopIteration()

    # constructor
    def __init__(self):
        self.layout = list()

    def getNewID(self):
        Conveyor.currentID += 1
        return Conveyor.currentID - 1

    def addSection(self, section):
        self.layout.append(section)

    def addBox(self, newBox):
        firstElement = self.layout[0]
        if not firstElement.hasBox():
            firstElement.setBox(newBox)

    def moveConveyor(self, distanceToMove):

        for i in range(0, distanceToMove):
            sIterator = StationIterator(self)
            iter(sIterator)
            for s in sIterator:
                s.package(s)
            # generate a list of all the boxes on the conveyor currently
            currentBoxes = list()
            index = 0
            for section in self.layout:
                if section.hasBox():
                    currentBox = section.getBox()
                    currentBoxes.append(currentBox)
                else:
                    currentBoxes.append('    ')
                index += 1
            for section in self.layout:
                section.removeBox()

            for box in currentBoxes:
                if currentBoxes.index(box) < len(self.layout) - 1 and box != '    ':
                    self.layout[currentBoxes.index(box) + 1].setBox(box)

            for box in currentBoxes:
                if currentBoxes.index(box) < len(self.layout) - 1 and box != '    ' and isinstance(self.layout[currentBoxes.index(box) + 1], Station):
                        self.layout[currentBoxes.index(box) + 1].load(box)

            print(self)

    def __str__(self):
        upperBoxString = ""
        lowerBoxString = ""
        layoutString = ""
        for section in self.layout:
            layoutString += section.pattern
            if section.hasBox():
                currentBox = section.getBox()
                upperBoxString += str(currentBox.id).ljust(4)
                lowerBoxString += str(currentBox.units).ljust(4)
            else:
                upperBoxString += ('    ')
                lowerBoxString += ('    ')
        return upperBoxString + '\n' + lowerBoxString + '\n' + layoutString

