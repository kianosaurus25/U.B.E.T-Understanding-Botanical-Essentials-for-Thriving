import time
import json


# This loads and updates the json files.
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


def plant_category(plant_data, plant_library):
    print()
    print("******PLANT CATEGORY******")
    time.sleep(1)
    for i in range(len(plant_library)):
        print(plant_library[i]["name"])
    category = input("Enter plant category: ").upper()

    if category not in plant_data:
        print("Invalid category (Either doesn't exist, or you just spelled it wrong).")
        time.sleep(3)
        return None

    return category


def plant_environment():
    print()
    print("******PLANT ENVIRONMENT******")
    time.sleep(3)
    print("Enter plant conditions:")

    light = input("Light(direct,indirect, or filtered): ")
    water = input("Water(moist,damp, or wet): ")
    soil = input("Soil(nutrient rich, peat rich, well drained or soggy): ")

    return {
        "light": light,
        "water": water,
        "soil": soil
    }

# This checks if the user is taking good care of their plants using the plant data they have inserted.
def plant_care(category, check, plant_data):
    print()
    print("******ANALYZING******")
    time.sleep(3)
    # Get the correct care data from the given category
    correct = plant_data[category]

    # This loop loops for each care requirement
    for data in correct:
        # Get the correct value for each care requirement
        correctCare = correct[data]

        # tHe purpose of the check is to store the users input for each care requirement
        user = check[data]

        #Checks if the user is NOT taking care of their plant properly, or if the user left a blank input.
        if user == "" or user not in correctCare:
            print(f"{data} is bad!")
            print(f"It should be: {correctCare}")
            time.sleep(3)
            print()
        else: #User is good at taking care of their plant
            print(f"{data} is good!")
    

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
                                  ⣀⣴⢾⣿⡷⣦⣄⡀⠀⢀⣠⡴⠒⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⣶⠶⣦⣤⣀⣀⣠⡾⠋⠀⠸⡇⠀⠀⣈⡽⠞⠉⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠉⠛⠻⠶⣦⣤⣄⣀⣠⡾⠟⠀⠀⠀⠀⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⢀⣀⣀⣀⣻⣆⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⣠⣿⡿⠟⠛⠛⠛⠛⠓⠒⢫⣿⡿⠃
                ⣶⡾⠛⠛⠛⠛⠛⠛⠛⠛⢽⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣟⣋⣁⠀⠀⠀⠀⠀⢀⣠⡶⠟⠁⠀⠀
                ⠀⠉⠛⠶⣄⡀⠀⠀⣀⠀⢀⡖⠛⠛⢿⣿⣶⣤⣤⣴⣾⣿⠟⢉⠉⠙⣿⢧⢶⣺⠟⠋⠉⠀⠀⠀⠀⠀
                ⠀⠀⠀⣀⣤⠽⠿⠛⡟⠀⣿⠀⠿⠇⠀⣿⡇⠉⠉⠁⠙⡇⠸⠿⠇⠀⣽⡎⡇⢈⣻⡆⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠛⠶⠤⣄⣀⡇⠀⢿⣄⣀⣀⣠⣷⠃⣀⠀⠀⡤⠙⣦⣄⣀⣴⠟⠁⣿⠋⠉⠁⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠉⠉⠉⠉⠁⠀⠙⡦⠞⠁⠀⠈⠉⠉⠁⢀⣴⠃⠀⠀⠀⠀⣠⣾⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀
                ⠀⠀⢿⠳⣦⠤⠤⠴⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⡟⡽⠋⠁⠀⠀⠀⠀⠀⠀
                ⣀⣤⣜⡒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀
                ⠈⠻⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠙⠿⣦⡀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠉⠛⢶⣚⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣾⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣯⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣯⣿⣷⠇⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡟⠉⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⢿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⠇⠀⠀⠀⠀⠀⣠⣶⣦⣀⠀⠀⠀⠀⠈⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⣀⣴⣫⠟⠁⠉⠻⢷⣆⡀⠀⠀⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣦⣖⠖⠋⠉⠁⠀⠀⠀⠀⠀⠀⠈⠻⢶⣾⡿⢯⠭⠗⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠟⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠄⠀⠀⠀⠀⠀
                                                  
    """

    print(asciART)
# Shows users menu options.
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
        category = plant_category(plant_data, plant_library)
        if category:
            check = plant_environment()
            plant_care(category, check, plant_data)

    elif menu == 3:
        program_on = False
    else:
        print("Invalid input! Please try again")
        print()




