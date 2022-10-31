from johnson_noah.Conveyor import Conveyor
from johnson_noah.StationIterator import StationIterator
from johnson_noah.Box import Box
from johnson_noah.Belt import Belt
from johnson_noah.Station import Station
from johnson_noah.LoadStrategy import LoadStrategy
from johnson_noah.PackagingStrategy import PackagingStrategy

currentIndex = 0


def cleanInput(prompt):
    result = input(prompt)
    # strips out blank lines in input
    while result == '':
        result = input()
    return result

def startingConveyor(conveyor):
    belt1 = Belt()
    belt2 = Belt()
    station1 = Station(1)
    belt3 = Belt()
    belt4 = Belt()
    station2 = Station(2)
    conveyor.layout.append(belt1)
    conveyor.layout.append(belt2)
    conveyor.layout.append(station1)
    conveyor.layout.append(belt3)
    conveyor.layout.append(belt4)
    conveyor.layout.append(station2)
    print(conveyor)
    return conveyor



def main():
    conveyor = Conveyor()
    conveyor = startingConveyor(conveyor)

    choice = -10
    while choice != 0:
        displayMenu()
        choice = getUserInput()

        # add default box
        if choice == 1:
            newID = conveyor.getNewID()
            newBox = Box(newID, 10, 0)
            conveyor.addBox(newBox)
            print(conveyor)

        # update one time
        elif choice == 2:
            conveyor.moveConveyor(1)

        # update X number of times
        elif choice == 3:
            try:
                numToMove = cleanInput("How many updates:> ")
                numToMove = int(numToMove)
                conveyor.moveConveyor(numToMove)
            except:
                print("Please, input a positive integer")

        # print out station details
        elif choice == 4:
            sIterator = StationIterator(conveyor)
            iter(sIterator)
            for s in sIterator: # GRADING: LOOP_STATION
                print(repr(s))

        # make a new box of any size
        elif choice == 5:
            try:
                choice1 = cleanInput("How many units:> ")
                units = int(choice1)
                if units < 1:
                    print("Please, input a positive integer")
            except:
                print("Please, input a positive integer")
            if units > 0:
                newID = conveyor.getNewID()
                newBox = Box(newID, units, 0)
                conveyor.addBox(newBox)
                print(conveyor)

        # make test system
        elif choice == 6:

            testConveyor = Conveyor()

            # belt 1
            belt = Belt()
            testConveyor.layout.append(belt)

            # station 1
            station1LoadStrategy = LoadStrategy("TestLoading1") # Loading: None, Packaging: None
            station1PackagingStrategy = PackagingStrategy("TestPackaging1")
            station1 = Station(1, station1LoadStrategy, station1PackagingStrategy)
            testConveyor.layout.append(station1)

            # belt 2
            belt2 = Belt()
            testConveyor.layout.append(belt2)

            # belt 3
            belt3 = Belt()
            testConveyor.layout.append(belt3)

            # station 2
            station2LoadStrategy = LoadStrategy("TestLoading2") # Loading: Basic 2, Packaging: Basic 2
            station2PackagingStrategy = PackagingStrategy("TestPackaging2")
            station2 = Station(2, station2LoadStrategy, station2PackagingStrategy)
            testConveyor.layout.append(station2)

            # belt 4
            belt4 = Belt()
            testConveyor.layout.append(belt4)

            # belt 5
            belt5 = Belt()
            testConveyor.layout.append(belt5)

            # station 3
            station3LoadStrategy = LoadStrategy("TestLoading3") # Loading: Percentage 0.5, Restricted amt 3, range 0-1000
            station3PackagingStrategy = PackagingStrategy("TestPackaging3")
            station3 = Station(3, station3LoadStrategy, station3PackagingStrategy)
            testConveyor.layout.append(station3)
            conveyor = testConveyor
            print(testConveyor)

        # make new system
        elif choice == 7:
            newConveyor = Conveyor()
            stationNum = 1
            addAnotherComponent = 'y'
            while addAnotherComponent != 'n':
                try:
                    userChoice = cleanInput("Belt (1) or Station (2):> ")
                    try:
                        int(userChoice)
                    except:
                        raise TypeError
                    # create belt
                    if userChoice == '1':
                        length = cleanInput("Length:> ")
                        length = int(length)
                        for i in range (length):
                            belt = Belt()
                            newConveyor.layout.append(belt)

                    # create station
                    elif userChoice == '2':
                        loadBehavior = "None"
                        packagingBehavior = "None"
                        loadBehaviorChoice = cleanInput("Load behavior: None (1), Basic (2), or Percentage (3):> ")
                        try:
                            int(loadBehaviorChoice)
                        except:
                            raise TypeError
                        if loadBehaviorChoice == '2':
                            loadBehavior = LoadStrategy("Basic")
                        elif loadBehaviorChoice == '3':
                            loadBehavior = LoadStrategy("Percentage")

                        if not 1 <= int(loadBehaviorChoice) <= 3:
                            raise TypeError

                        packagingBehaviorChoice = cleanInput("Packaging behavior: None (1), Basic (2), or Restricted (3):> ")
                        if packagingBehaviorChoice == '2':
                            packagingBehavior = PackagingStrategy("Basic")
                        elif packagingBehaviorChoice == '3':
                            packagingBehavior = PackagingStrategy("Restricted")

                        if not 1 <= int(packagingBehaviorChoice) <= 3:
                            raise TypeError

                        newStation = Station(stationNum, loadBehavior, packagingBehavior)
                        newConveyor.layout.append(newStation)
                        stationNum += 1
                    else:
                        print("Input an option in the range 1-2")
                except:
                    print("Cannot accept value")
                addAnotherComponent = cleanInput("\nAdd another component (n to stop):> ")
            conveyor = newConveyor
            print(conveyor)

        # debug/check for D in SOLID in __str__
        elif choice == -1:
            # box 1
            newID = conveyor.getNewID()
            box1 = Box(newID, 10, 0)

            # box 2
            newID = conveyor.getNewID()
            box2 = Box(newID, 10, 0)

            # box 3
            newID = conveyor.getNewID()
            box3 = Box(newID, 10, 0)

            # belt 1
            belt1 = Belt()

            # belt 2
            station1 = Station(1)

            belt1.setBox(box1)
            station1.setBox(box2)
            conveyor.addBox(box3)

            print(box1)
            print(box2)
            print(belt1)
            print(station1)
            print(conveyor)

        elif choice == 0 or '0':
            choice = 0
        else:
            print("Input an option in the range 0-7")


def displayMenu():
    menu = "\n" \
           "1) Add Default Box\n" \
           "2) Move Belt One Time Unit\n" \
           "3) Move Belt X Time Units\n" \
           "4) Show Station Details\n" \
           "5) Add Box\n" \
           "6) Make Tester Conveyer Belt\n" \
           "7) Make New Conveyer Belt\n" \
           "0) Quit\n"
    print(menu)


def getUserInput():
    choice = -10
    while choice != 0:
        try:
            choice = cleanInput("Choice:> ")
            try:
                choice = int(choice)
                if choice in range(-1, 8):
                    return choice
                else:
                    print('Input an option in the range 0-7')
            except ValueError:
                print("Please, input a positive integer")
        except:
            import traceback
            print(traceback.format_exc())
        displayMenu()
    return choice


if __name__ == '__main__':
    main()
