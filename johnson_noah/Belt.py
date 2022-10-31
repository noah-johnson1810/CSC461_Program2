class Belt:
    """
    Author: Noah Johnson
    Description: Python Conveyor Belt Project, Belt Class
    """
    # this belt's layout character pattern
    pattern = '----'

    def __init__(self):
        """
        constructor for a new belt, sets it to have no box
        @return: none
        """
        self.currentBox = '    '

    def __str__(self):
        """
        creates a string representation of this belt
        @return: string representation of this belt
        """
        returnString = ""
        currentBox = self.getBox()
        returnString += str(currentBox) + '\n' + str(self.pattern)
        return returnString

    def getBox(self):
        """
        gets the current box on the belt
        @return: the current box on the belt
        """
        return self.currentBox

    def hasBox(self):
        """
        determines whether the belt has a box on it
        @return: true if it has a box, false if not
        """
        return not self.currentBox == '    '

    def removeBox(self):
        """
        removes the current box on the belt
        @return: none
        """
        self.currentBox = '    '

    def setBox(self, newBox):
        """
        sets the box currently on this belt
        @param newBox: the box to be put on the belt
        @return: none
        """
        self.currentBox = newBox

