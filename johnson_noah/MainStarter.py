from johnson_noah.Section import Box, Conveyor

currentIndex = 0


def cleanInput(prompt):
    result = input(prompt)
    # strips out blank lines in input
    while result == '':
        result = input()
    return result


def main():
    conveyor = Conveyor()
    choice = -10
    while choice != 0:
        print(conveyor)
        displayMenu()
        choice = getUserInput()
        # add default box
        if choice == 1:
            newID = conveyor.getNewID()
            newBox = Box(newID, 2, 0)
            conveyor.addBox(newBox)

    # update one time
        elif choice == 2:
            conveyor.moveConveyor(1)

# update X number of times
        elif choice == 3:
            print("TODO")

# print out station details
        elif choice == 4:
            print("TODO")

# make a new box of any size
        elif choice == 5:
            print("TODO")

# make new system
        elif choice == 6:
            print("TODO")

        # make new system
        elif choice == 7:
            print("TODO")

# debug/check for D in SOLID in __str__
        elif choice == -1:
            print("TODO")

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
                if choice in range(-1, 7):
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
