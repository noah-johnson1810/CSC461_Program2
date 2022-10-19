def cleanInput(prompt):
    result = input(prompt)
    # strips out blank lines in input
    while result == '':
        result = input( )

    return result

def main( ):
    menu = "\n" \
           "1) Add Default Box\n" \
           "2) Move Belt One Time Unit\n" \
           "3) Move Belt X Time Units\n" \
           "4) Show Station Details\n" \
           "5) Add Box\n" \
           "6) Make Tester Conveyer Belt\n" \
           "7) Make New Conveyer Belt\n" \
           "0) Quit\n"


    choice = -1
    while choice != 0:

        print( menu )
        choice = cleanInput( "Choice:> " )

        # add default box
        if choice == 1:
            print( "TODO" )

        # update one time
        elif choice == 2:
            print( "TODO" )

        # update X number of times
        elif choice == 3:
            print( "TODO" )

        # print out station details
        elif choice == 4:
            print( "TODO" )

        # make a new box of any size
        elif choice == 5:
            print( "TODO" )

        # make new system
        elif choice == 6:
            print( "TODO" )

        # make new system
        elif choice == 7:
            print( "TODO" )

        # debug/check for D in SOLID in __str__
        elif choice == -1:
            print( "TODO" )

        elif choice == 0 or '0':
            choice = 0
        else:
            print( "Input an option in the range 0-7" )


if __name__ == '__main__':
    main( )
