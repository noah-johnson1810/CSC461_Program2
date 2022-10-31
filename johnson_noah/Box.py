class Box:
    def __init__(self, id, maxLoad, units=10):
        self.id = id
        self.maxLoad = maxLoad
        self.units = units
        self.position = 0

    def __str__(self):
        return str(self.id) + '\n' + str(self.units)