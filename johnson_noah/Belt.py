class Belt:
    pattern = '----'
    def hasBox(self):
        return not self.currentBox == '    '

    def setBox(self, newBox):
        self.currentBox = newBox

    def getBox(self):
        return self.currentBox

    def removeBox(self):
        self.currentBox = '    '

    def __init__(self):
        self.currentBox = '    '

    def __str__(self):
        returnString = ""
        currentBox = self.getBox()
        returnString += str(currentBox) + '\n' + str(self.pattern)
        return returnString