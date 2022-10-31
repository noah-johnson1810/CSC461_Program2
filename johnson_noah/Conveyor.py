from johnson_noah.Station import Station
from johnson_noah.StationIterator import StationIterator
from johnson_noah.ConveyorIterator import ConveyorIterator

class Conveyor:
    """
    Author: Noah Johnson
    Description: Python Conveyor Belt Project, Conveyor class
    """

    # initialize the current ID (for the program) to 1
    currentID = 1

    def __init__(self):
        """
        constructor for the conveyor class
        @return: none
        """
        self.layout = list()

    def __str__(self):
        """
        to-string for conveyor class
        @return: string containing representation
        """
        upperBoxString = ""
        lowerBoxString = ""
        layoutString = ""

        conveyorIterator = ConveyorIterator(self)
        iter(conveyorIterator)
        for section in conveyorIterator: # GRADING: LOOP_ALL
            layoutString += section.pattern
            if section.hasBox():
                currentBox = section.getBox()
                upperBoxString += str(currentBox.id).ljust(4)
                lowerBoxString += str(currentBox.units).ljust(4)
            else:
                upperBoxString += ('    ')
                lowerBoxString += ('    ')
        return upperBoxString + '\n' + lowerBoxString + '\n' + layoutString

    def addBox(self, newBox):
        """
        adds a new box to the conveyor
        @param newBox: the new box to be added to the conveyor
        @return: none
        """
        firstElement = self.layout[0]
        if not firstElement.hasBox():
            firstElement.setBox(newBox)

    def addSection(self, section):
        """
        adds a new section to the conveyor
        @param section: the new section to be added to the conveyor
        @return: none
        """
        self.layout.append(section)

    def getNewID(self):
        """
        gets the current ID for the box and then increments it by one so that it won't be used again
        @return: the old current ID (before incrementing)
        """
        Conveyor.currentID += 1
        return Conveyor.currentID - 1

    def moveConveyor(self, distanceToMove):
        """
        moves the conveyor by the amount specified
        @param distanceToMove: the distance to move the conveyor
        @return: none
        """
        # move as many times as the specified distance
        for i in range(0, distanceToMove):
            # custom iterator
            sIterator = StationIterator(self) # GRADING: ITER_ALL
            iter(sIterator)
            # package from last update before loading next
            for s in sIterator: # GRADING: LOOP_ALL
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
            # clear layout
            for section in self.layout:
                section.removeBox()
            # put boxes back in their correct (updated) positions
            for box in currentBoxes:
                if currentBoxes.index(box) < len(self.layout) - 1 and box != '    ':
                    self.layout[currentBoxes.index(box) + 1].setBox(box)
            # if the box isn't out of range and is going to a station, load it
            for box in currentBoxes:
                if currentBoxes.index(box) < len(self.layout) - 1 and box != '    ' \
                        and isinstance(self.layout[currentBoxes.index(box) + 1], Station):
                        self.layout[currentBoxes.index(box) + 1].load(box)
            print(self)