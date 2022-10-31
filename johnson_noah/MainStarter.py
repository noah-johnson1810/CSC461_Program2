##
#  Author: Noah Johnson
#  Class: CSC 461 - Fall 2022
#  Description: Python Project for Programming Languages (CSC 461) - ConveyorBelt. This is a console-style conveyor belt
#  builder/simulator. The belt is made up of belts, which just moves boxes along, and stations, which load and package
#  the boxes. It displays a menu for a user to select what they want to do to the conveyor. They can add a
#  default box, or a custom box with a custom capacity, move the belt 1 or custom time units, show station details,
#  create a preset "testing" conveyor belt, or even build a custom conveyor belt with customizable loading and packaging
#  settings, and a unique layout chosen by the user.
#
#  Last tier passed: 9c / tierless / all
#
# Checklist:
# Grading tags in for all lines marked with *       X
#
# Tierless str meets D in SOLID (hidden test)*		X
# Check if done, but not all tiers are passing		___ (all tiers pass)
#
# 1. Initial Show system\Got it compiling
# Menu\initial system working						X
# Bad input handled								    X
#
# 2. Add Default Box
# Added and shown properly						    X
# Second+ box ignored								X
#
# 3. Basic Update
# Moves along belts								    X
# Moves to next station\belt						X
# Drops off the end when reached					X
# String format correct							    X
# Iterator used*									X
#
# 4. Multi Update
# Updates correct amount							X
# Bad input handled								    X
# String format correct							    X
#
# 5. Show station details (default)
# Shows stations details properly 				    X
# Iterator used*									X
# 6. Add box
# Added and shown properly						    X
# Second+ box ignored								X
# Bad input handled								    X
#
# 7. Tester Conveyer part 1
# Initial system and station details correct 		X
# A single box still able to be added				X
# Update with one default box works				    X
# Loading works 									X
# Formatting correct 								X
#
# 8. Tester Conveyer part 2
# Packaging works 								    X
# Formatting correct 								X
# Strategy pattern for loading*					    X
# Strategy pattern for packaging*					X
#
#
# 9. Custom belt
# String formatting correct						    X
# Everything still works 							X
# Bad input handled 								X
#


# import statements

from johnson_noah.Conveyor import Conveyor
from johnson_noah.StationIterator import StationIterator
from johnson_noah.Box import Box
from johnson_noah.Belt import Belt
from johnson_noah.Station import Station
from johnson_noah.LoadStrategy import LoadStrategy
from johnson_noah.PackagingStrategy import PackagingStrategy



# Description: provided function to get clean input (ignoring white space)
# Parameter: prompt - the message to display to the user
# Return: result - the input

def cleanInput(prompt):
    result = input(prompt)
    # strips out blank lines in input
    while result == '':
        result = input()
    return result



# Description: this function simply packages the code to create the starting conveyor for the program
# Parameter: conveyor - the conveyor (of type Conveyor) to create this layout in
# Return: conveyor - the conveyor with the starting layout added

def startingConveyor(conveyor):
    # create each layout piece
    belt1 = Belt()
    belt2 = Belt()
    station1 = Station(1)
    belt3 = Belt()
    belt4 = Belt()
    station2 = Station(2)
    # append each piece to the conveyor's layout list
    conveyor.layout.append(belt1)
    conveyor.layout.append(belt2)
    conveyor.layout.append(station1)
    conveyor.layout.append(belt3)
    conveyor.layout.append(belt4)
    conveyor.layout.append(station2)
    print(conveyor)
    return conveyor



# Description: displays the menu, handles user input and error checking, and organizes function calling and output
# Parameter: none
# Return: none

def main():
    # create initial conveyor, initialize to starting conveyor
    conveyor = Conveyor()
    conveyor = startingConveyor(conveyor)

    # initialize choice to enter loop, continue displaying menu until user enters 0
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
            # initialize custom station iterator
            sIterator = StationIterator(conveyor)
            iter(sIterator)
            for s in sIterator: # GRADING: LOOP_STATION
                print(repr(s))

        # make a new box of any size
        elif choice == 5:
            # get user input for units, check to make sure it's a positive integer
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

            # initialize new conveyor
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
            # preset load strategy for test station 2
            station2LoadStrategy = LoadStrategy("TestLoading2") # Loading: Basic 2, Packaging: Basic 2
            # preset packaging strategy for test station 2
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
            # preset load strategy for test station 3
            station3LoadStrategy = LoadStrategy("TestLoading3") # Loading: Percentage 0.5, Restricted amt 3, range 0-1000
            # preset packaging strategy for test station 3
            station3PackagingStrategy = PackagingStrategy("TestPackaging3")
            station3 = Station(3, station3LoadStrategy, station3PackagingStrategy)
            testConveyor.layout.append(station3)

            # set the main conveyor to be this one
            conveyor = testConveyor
            print(testConveyor)

        # make new system
        elif choice == 7:
            # create new conveyor
            newConveyor = Conveyor()
            #initialize station number to start at 1
            stationNum = 1
            addAnotherComponent = 'y'
            while addAnotherComponent != 'n':
                # get user input for belt or station
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
                        # one belt for each length they want
                        for i in range (length):
                            belt = Belt()
                            newConveyor.layout.append(belt)

                    # create station
                    elif userChoice == '2':
                        loadBehavior = "None"
                        packagingBehavior = "None"
                        # get input for load behavior
                        loadBehaviorChoice = cleanInput("Load behavior: None (1), Basic (2), or Percentage (3):> ")
                        try:
                            int(loadBehaviorChoice)
                        except:
                            raise TypeError
                        if loadBehaviorChoice == '2':
                            loadBehavior = LoadStrategy("Basic")
                        elif loadBehaviorChoice == '3':
                            loadBehavior = LoadStrategy("Percentage")

                        # must be between 1 and 3
                        if not 1 <= int(loadBehaviorChoice) <= 3:
                            raise TypeError

                        # get input for packaging behavior
                        packagingBehaviorChoice = cleanInput("Packaging behavior: None (1), Basic (2), or Restricted (3):> ")
                        if packagingBehaviorChoice == '2':
                            packagingBehavior = PackagingStrategy("Basic")
                        elif packagingBehaviorChoice == '3':
                            packagingBehavior = PackagingStrategy("Restricted")

                        # must be between 1 and 3
                        if not 1 <= int(packagingBehaviorChoice) <= 3:
                            raise TypeError

                        newStation = Station(stationNum, loadBehavior, packagingBehavior)
                        newConveyor.layout.append(newStation)
                        stationNum += 1
                    else:
                        print("Input an option in the range 1-2")
                except:
                    print("Cannot accept value")

                # get input for whether to add another component to the custom conveyor
                addAnotherComponent = cleanInput("\nAdd another component (n to stop):> ")

            # set the main conveyor to be this conveyor
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

            # set the boxes in the belt/station/conveyor
            belt1.setBox(box1)
            station1.setBox(box2)
            conveyor.addBox(box3)

            # print each one
            # GRADING: TO_STR
            print(box1)
            print(box2)
            print(belt1)
            print(station1)
            print(conveyor)

        elif choice == 0 or '0':
            choice = 0
        # warn invalid user input
        else:
            print("Input an option in the range 0-7")



# Description: helper function to display the menu
# Parameter: none
# Return: none

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



# Description: gets user input in the range -1 to 7 inclusive, displays menu until appropriate choice is made
# Parameter: none
# Return: choice - the user's input

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



# run main
if __name__ == '__main__':
    main()
