filename = "AuthorizedVehicles.txt"

default_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 
                    'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500']

try:  
    with open(filename, 'x') as file:
        for vehicle in default_vehicles:
            file.write(vehicle + '\n')
except FileExistsError:
    pass 

def read_vehicles():
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def write_vehicles(vehicles):
    with open(filename, 'w') as file:
        for vehicle in vehicles:
            file.write(vehicle + '\n')

while True:
    print('********************************')
    print('AutoCountry Vehicle Finder v0.2')
    print('********************************')
    print('Please Enter the following number below from the menu:')
    print('1. PRINT all Authorized Vehicles')
    print('2. SEARCH for Authorized Vehicle')
    print('3. ADD Authorized Vehicle')
    print('4. DELETE Authorized Vehicle')
    print('5. Exit')

    query = input()

    if query == '1':
        vehicles = read_vehicles()
        print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
        for vehicle in vehicles:
            print(vehicle)
    elif query == '2':
        vehicles = read_vehicles()
        query2 = input("Please Enter the full Vehicle name: ")
        if query2 in vehicles:
            print(query2 + ' is an authorized vehicle.')
        else:
            print(query2 + ' is not an authorized vehicle. Please check the spelling and try again.')
    elif query == '3':
        query3 = input("Please Enter the full vehicle name you would like to add: ")
        vehicles = read_vehicles()
        if query3 not in vehicles:
            vehicles.append(query3)
            write_vehicles(vehicles)
            print('You have added "' + query3 + '" as an authorized vehicle.')
        else:
            print(query3 + " is already in the list.")
    elif query == '4':
        query4 = input("Please Enter the full Vehicle name you would like to REMOVE: ")
        query5 = input('Are you sure you would like to remove "' + query4 + '" from the Authorized Vehicles List? (yes/no) ')
        if query5.lower() == "yes":
            vehicles = read_vehicles()
            if query4 in vehicles:
                vehicles.remove(query4)
                write_vehicles(vehicles)
                print('You have removed "' + query4 + '" as an authorized vehicle.')
            else:
                print(query4 + " is not in the list.")
    elif query == '5':
        print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
        break
    else:
        print('Invalid option. Please enter a valid number from the menu.')
