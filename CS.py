mport time

program_on = True
while program_on == True:
    print("MENU")
    print("WELCOME TO U.B.E.T")
    print("1) View plant group library ")
    print("2) Identify plant needs ")
    print("3) Quit")

    menu = int(input("What would you like to do <3?: "))
    if menu == 1:
        print("1]ANGIOSPERMS")
        print("2]BRYOPHYTA")
        print("3]GYMNOSPERMS")
        print("4]PTERIDOPHYTES")
        print("5]CYCADOPHYTA")
        print("6]HORSETAILS")
        print("7]LIVERWORTS")
        print("8]TREES")
        plant_category = int(input("See description of which plant group?"))
        if plant_category == 1:
            print("goo goo gaga")

    elif menu == 2:
        print()
        print("What category best describes your plant?")
        print("1]ANGIOSPERMS")
        print("2]BRYOPHYTA")
        print("3]GYMNOSPERMS")
        print("4]PTERIDOPHYTES")
        print("5]CYCADOPHYTA")
        print("6]HORSETAILS")
        print("7]LIVERWORTS")
        print("8]TREES")
        time.sleep(3)

    elif menu == 3:
        program_on = False
    else:
        print("Invalid input! Please try again")
        print()
