import time
import json



try:
    with open("plant_library.json", "r") as file:
        plant_library = json.load(file)

    with open("plant_data.json", "r") as file:
        plant_data = json.load(file)

except FileNotFoundError as e:
    print("Error: The file 'data.json' was not found.")
    plant_library = []
    plant_data = {}

except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")
    plant_library = []
    plant_data = {}


def view_library(plant_library):
    if not plant_library:
        print("Plant library is empty.")
        return

    print("PLANT LIBRARY:")
    for i in range(len(plant_library)):
        print(f"{i + 1}. {plant_library[i]["name"]}")

    print()

    try:
        choice = int(input("Choose a plant: "))
        if choice < 1 or choice > len(plant_library):
            print("Invalid choice.")
            return
    except:
        print("Please enter a number.")
        return

    plant = plant_library[choice - 1]

    print("PLANT INFO")
    print("Name:", plant["name"])
    print("Description:", plant["description"])
    print("Care:", plant["care"])
    print("Fact:", plant["fact"])
    print()


def plant_category(plant_data):
    category = input("Enter plant category: ").upper()

    if category not in plant_data:
        print("Invalid category.")
        return None

    return category


def plant_environment():
    print("Enter plant conditions:")

    light = input("Light: ")
    water = input("Water: ")
    soil = input("Soil: ")

    return {
        "light": light,
        "water": water,
        "soil": soil
    }


def plant_care(category, check, plant_data):
    correct = plant_data[category]

    for data in correct:
        correctCare = correct[data]
        user = check[data]

        if user not in correctCare:
            print(f"{data} is bad")
            print(f"Your plant should have: {correctCare}")
        else:
            print(f"{data} is gud")
    

program_on = True
while program_on == True:
    time.sleep(0.5)
    asciART = """ 
     █     █░▓█████  ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████    ▄▄▄█████▓ ▒█████ 
    ▓█░ █ ░█░▓█   ▀ ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀    ▓  ██▒ ▓▒▒██▒  ██
    ▒█░ █ ░█ ▒███   ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███      ▒ ▓██░ ▒░▒██░  ██
    ░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄    ░ ▓██▓ ░ ▒██   ██
    ░░██▒██▓ ░▒████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒     ▒██▒ ░ ░ ████▓▒
    ░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░     ▒ ░░   ░ ▒░▒░▒░
      ▒ ░ ░   ░ ░  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░       ░      ░ ▒ ▒░
      ░   ░     ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░        ░      ░ ░ ░ ▒ 
        ░       ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░                ░ ░ 
                            ░                                                                                                                                                 
                       █    ██       ▄▄▄▄        ▓█████      ▄▄▄█████▓              
                       ██  ▓██▒     ▓█████▄      ▓█   ▀      ▓  ██▒ ▓▒              
                      ▓██  ▒██░     ▒██▒ ▄██     ▒███        ▒ ▓██░ ▒░              
                      ▓▓█  ░██░     ▒██░█▀       ▒▓█  ▄      ░ ▓██▓ ░               
                      ▒▒█████▓  ██▓ ░▓█  ▀█▓ ██▓ ░▒████▒ ██▓   ▒██▒ ░               
                      ░▒▓▒ ▒ ▒  ▒▓▒ ░▒▓███▀▒ ▒▓▒ ░░ ▒░ ░ ▒▓▒   ▒ ░░                 
                      ░░▒░ ░ ░  ░▒  ▒░▒   ░  ░▒   ░ ░  ░ ░▒      ░                  
                       ░░░ ░ ░  ░    ░    ░  ░      ░    ░     ░                    
                         ░       ░   ░        ░     ░  ░  ░                         
                                 ░        ░   ░           ░      
        """
    print(asciART)
    time.sleep(0.5)
    asciART =  """          
                       ███▄ ▄███▓▓█████  ███▄    █  █    ██ 
                      ▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █  ██  ▓██▒
                      ▓██    ▓██░▒███   ▓██  ▀█ ██▒▓██  ▒██░
                      ▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒▓▓█  ░██░
                      ▒██▒   ░██▒░▒████▒▒██░   ▓██░▒▒█████▓ 
                      ░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ 
                      ░  ░      ░ ░ ░  ░░ ░░   ░ ▒░░░▒░ ░ ░ 
                      ░      ░      ░      ░   ░ ░  ░░░ ░ ░ 
                      ░      ░  ░         ░    ░      
                                                  
    """

    print(asciART)

    time.sleep(0.5)
    print("1) View plant group library ")
    time.sleep(0.5)
    print("2) Identify plant needs ")
    time.sleep(0.5)
    print("3) Quit")
    time.sleep(0.5)
    menu = int(input("What would you like to do?: "))
    if menu == 1:
        view_library(plant_library)
    elif menu == 2:
        category = plant_category(plant_data)
    if category:
        check = plant_environment()
        plant_care(category, check, plant_data)

    elif menu == 3:
        program_on = False
    else:
        print("Invalid input! Please try again")
        print()




