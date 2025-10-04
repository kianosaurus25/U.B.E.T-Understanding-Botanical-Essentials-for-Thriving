import time

plant_categories = [ "ANGIOSPERMS", "BRYOPHYTA", "GYMNOSPERMS", "PTERIDOPHYTES", "CYCADOPHYTA", "HORSETAILS", "LIVERWORTS", "TREES" ]

program_on = True
while program_on:
    print("MENU")
    print("WELCOME TO U.B.E.T")
    print("1) View plant group library ")
    print("2) Identify plant needs ")
    print("3) Quit")

    menu = int(input("What would you like to do <3?: "))
    if menu == 1:
        for i in range(len(plant_categories)):
            print(f"{i + 1}] {plant_categories[i]}")
        library_category = int(input("See description of which plant group?"))
        if library_category == 1:
            print("goo goo gaga")

    elif menu == 2:
        def get_category():
            for i in range(len(plant_categories)):
                print(f"{i + 1}] {plant_categories[i]}")
            category = int(input("Please enter your plant's category"))
            return category

        def get_environment():
            environment = input("What is environment is your plant currently in?")
            return environment

        def get_care(category, environment):
            care = input("sah")
            return care

        plant_category = get_category()
        plant_environment = get_environment()
        plant_care = get_care(plant_category, plant_environment)
        print(plant_category)


