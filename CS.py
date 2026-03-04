import time

plant_data = {
"ANGIOSPERMS": {
        "light": "direct/indirect sun",
        "water": "moist",
        "soil": "nutrient-rich"
    },
    "BRYOPHYTA": {
        "light": "indirect sun",
        "water": "damp",
        "soil": "peat-rich"
    },
    "GYMNOSPERMS": {
        "light": "full sun",
        "water": "moderate",
        "soil": "well drained"
    },
    "PTERIDOPHYTES": {
        "light": "filtered",
        "water": "damp",
        "soil": "well drained"
    },
    "CYCADOPHYTA": {
        "light": "avoid harsh sun",
        "water": "when top soil dry",
        "soil": "NPK fertilizer"
    },
    "HORSETAILS": {
        "light": "sun/partial",
        "water": "wet/moist",
        "soil": "well-drained"
    },
    "LIVERWORTS": {
        "light": "shade",
        "water": "constant moisture",
        "soil": "moist "
    },
    "TREES": {
        "light": "sun",
        "water": "moderate",
        "soil": "well-drained"
    }
}

plant_library = [
    {
        "name": "Angiosperms",
        "description": "Flowering plants that bear flowers and fruits.",
        "care": "Give direct or indirect sunlight, keep soil moist (not waterlogged), and use nutrient-rich soil."
    },
    {
        "name": "Bryophyta (Mosses)",
        "description": "Small plants that grow in damp woodland or moist areas.",
        "care": "Keep environment damp, provide bright indirect light, and use nutrient-rich soil like peat."
    },
    {
        "name": "Gymnosperms",
        "description": "Vascular plants that produce seeds and pollen instead of spores.",
        "care": "Provide full sun, well-draining soil, and proper moisture. Avoid overly wet soil to prevent disease."
    },
    {
        "name": "Pteridophytes (Ferns)",
        "description": "Plants with roots, stems, and leaves.",
        "care": "Place in filtered light, keep soil damp, increase humidity, use well-draining mix, and fertilize lightly in growing season."
    },
    {
        "name": "Cycadophyta (Cycads)",
        "description": "Palm-like plants with thick trunks and evergreen leaves.",
        "care": "Water when the top 2 inches of soil dry, avoid harsh direct sun, use fertilizer with NPK + magnesium, and check for pests."
    },
    {
        "name": "Horsetails",
        "description": "Fern-like plants that grow in damp or wet areas.",
        "care": "Provide moist to wet soil, full sun to partial shade, and consistent moisture. Use pots/barriers to prevent invasiveness."
    },
    {
        "name": "Liverworts",
        "description": "Small plants thriving in cool, shaded, humid environments.",
        "care": "Keep consistently moist, avoid direct sunlight, and protect from drying winds."
    },
    {
        "name": "Trees",
        "description": "Large plants that grow in many climates with deep root systems.",
        "care": "Use well-drained soil, water regularly when young, give full sun to partial shade, prune for health, and mulch the base."
    }
]
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

def plant_category():

def plant_environment():
    
def  plant_care():
    
program_on = True
while program_on == True:
    print("MENU")
    print("WELCOME TO U.B.E.T")
    print("1) View plant group library ")
    print("2) Identify plant needs ")
    print("3) Quit")

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



