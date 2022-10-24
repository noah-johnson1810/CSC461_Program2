class Station:
    pattern = 'XXXX'

    def __init__(self):
        x = 0


class Belt:
    pattern = '----'

    def __init__(self):
        x = 0


class Box:
    def __init__(self, id, maxLoad, units=10):
        self.id = id
        self.maxLoad = maxLoad
        self.units = units
        self.position = 0


class Conveyor:
    currentID = 1
    layout = list()
    boxes = list()
    length = 6

    # constructor
    def __init__(self):
        self.layout.clear()
        self.boxes.clear()
        belt1 = Belt()
        belt2 = Belt()
        station1 = Station()
        belt3 = Belt()
        belt4 = Belt()
        station2 = Station()
        self.layout.append(belt1)
        self.layout.append(belt2)
        self.layout.append(station1)
        self.layout.append(belt3)
        self.layout.append(belt4)
        self.layout.append(station2)

    def getNewID(self):
        self.currentID += 1
        return self.currentID - 1

    def addSection(self, section):
        self.layout.append(section)
        self.length = len(self.layout)

    def addBox(self, box):
        for box in self.boxes:
            if box.position == 0:
                return
        self.boxes.append(box)

    def trimExtraBoxes(self):
        for box in self.boxes:
            if box.position > len(self.layout) - 1:
                self.boxes.remove(box)

    def moveConveyor(self, distanceToMove):
        for box in self.boxes:
            box.position += distanceToMove
        self.trimExtraBoxes()

    def __str__(self):
        orderedBoxList = list()
        upperBoxString = ""
        lowerBoxString = ""
        layoutString = ""
        for section in self.layout:
            orderedBoxList.append('    ')
        for box in self.boxes:
            orderedBoxList.pop(box.position)
            orderedBoxList.insert(box.position, box)
        for box in orderedBoxList:
            if box != '    ':
                upperBoxString += str(box.id).ljust(4)
                lowerBoxString += str(box.units).ljust(4)
            else:
                upperBoxString += '    '
                lowerBoxString += '    '
        for section in self.layout:
            layoutString += section.pattern
        return upperBoxString + '\n' + lowerBoxString + '\n' + layoutString
