class Box:
    """
    Author: Noah Johnson
    Description: Python Conveyor Belt Project, Box class
    """

    def __init__(self, id, maxLoad, units):
        """
        constructor for new box, sets the id, maxLoad, and number of units
        @param id: the id for this box
        @param maxLoad: the maximum number of items that this box can hold
        @param units: the number of units currently in the box
        @return: none
        """
        self.id = id
        self.maxLoad = maxLoad
        self.units = units
        self.position = 0

    def __str__(self):
        """
        creates the string representation for this box
        @return: the string representation for this box
        """
        return str(self.id) + '\n' + str(self.units)