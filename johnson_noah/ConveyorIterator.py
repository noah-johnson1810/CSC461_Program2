class ConveyorIterator:
    """
    Author: Noah Johnson
    Description: Python Conveyor Belt project, Conveyor (All) Iterator
    """

    def __init__(self, conveyor):
        """
        sets the layout to the conveyor's layout
        @param: conveyor: the conveyor to iterate over
        @return: none
        """
        self.layout = conveyor.layout

    def __iter__(self): # GRADING: ITER_ALL
        """
        initializes the index to -1 as it is incremented before use to get to 0
        @param: conveyor: the conveyor to iterate over
        @return: self
        """
        self.__index = -1
        return self

    def __next__(self):
        """
        increases the index for the layout by 1 and returns that section of the layout
        @param: conveyor: the conveyor to iterate over
        @return: the layout section at the new index
        """
        self.__index += 1
        try:
            return self.layout[self.__index]
        except:
            raise StopIteration()