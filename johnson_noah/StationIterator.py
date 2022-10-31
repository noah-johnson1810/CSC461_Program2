from johnson_noah.Station import Station

class StationIterator:
    def __init__(self, conveyor):
        self.conveyor = conveyor

    def __iter__(self): # GRADING: ITER_STATION
        self.__index = -1
        return self

    def __next__(self):
        self.__index += 1
        try:
            while isinstance(self.conveyor.layout[self.__index], Station) is False:
                self.__index += 1
            return self.conveyor.layout[self.__index]
        except:
            raise StopIteration()