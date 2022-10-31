
from johnson_noah.Station import Station

class StationIterator:
    """
    Author: Noah Johnson
    Description: Python Conveyor Belt project, StationIterator class
    """

    def __init__(self, conveyor):
        """
        constructor for the StationIterator
        @type conveyor: Conveyor
        @param conveyor: the conveyor to iterate over
        @return: none
        """
        self.conveyor = conveyor


    def __iter__(self): # GRADING: ITER_STATION
        """
        sets the index to -1 since it is incremented before use to start at 0
        @return: none
        """
        self.__index = -1
        return self


    def __next__(self):
        """
        returns the next station after finding it by incrementing the index by 1 repeatedly
        @return: none
        """
        self.__index += 1
        try:
            while isinstance(self.conveyor.layout[self.__index], Station) is False:
                self.__index += 1
            return self.conveyor.layout[self.__index]
        except:
            raise StopIteration()