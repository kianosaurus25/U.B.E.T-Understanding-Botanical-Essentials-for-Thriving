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
   if menu ==  1:
        for i in range(len(plant_library)):
            print(f"{i + 1}. {plant_library[i]["name"]}")
        category =  int(input("Which category would you want to read about?"))
        n = category - 1
        print("Name:", plant_library[n]["name"])
        print("Description:", plant_library[n]["description"])
        print("Care:", plant_library[n]["care"])
        print()
#def plant_category():

#def plant_environment():
    
#def plant_care():
    
program_on = True
while program_on == True:
    print(" ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄         ▄ ")
    print("▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌       ▐░▌")
    print("▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░▌       ▐░▌")
    print("▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌")
    print("▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌")
    print("▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌")
    print("▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌")
    print("▐░▌       ▐░▌▐░▌          ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌")
    print("▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌")
    print("▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌")
    print(" ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀ ")
    time.sleep(2)
    print("===============WELCOME TO U.B.E.T==================")
    time.sleep(0.5)
    print("1) View plant group library ")
    time.sleep(0.5)
    print("2) Identify plant needs ")
    time.sleep(0.5)
    print("3) Quit")
    time.sleep(0.5)
    menu = int(input("What would you like to do?"))
    if menu == 1:
        view_library(plant_library)

    elif menu == 2:
        plant_category()
        plant_environment()
        plant_care()

    elif menu == 3:
        program_on = False
    else:
        print("Invalid input! Please try again")
        print()




