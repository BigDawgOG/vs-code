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

def print_vehicles():
    vehicles = read_vehicles()
    print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
    for vehicle in vehicles:
        print(vehicle)

def search_vehicle():
    vehicles = read_vehicles()
    query = input("Please Enter the full Vehicle name: ")
    if query in vehicles:
        print(query + ' is an authorized vehicle.')
    else:
        print(query + ' is not an authorized vehicle. Please check the spelling and try again.')

def add_vehicle():
    vehicles = read_vehicles()
    new_vehicle = input("Please Enter the full vehicle name you would like to add: ")
    if new_vehicle not in vehicles:
        vehicles.append(new_vehicle)
        write_vehicles(vehicles)
        print('You have added "' + new_vehicle + '" as an authorized vehicle.')
    else:
        print(new_vehicle + " is already in the list.")

def delete_vehicle():
    vehicles = read_vehicles()
    vehicle_to_remove = input("Please Enter the full Vehicle name you would like to REMOVE: ")
    confirmation = input('Are you sure you would like to remove "' + vehicle_to_remove + '" from the Authorized Vehicles List? (yes/no) ')
    if confirmation.lower() == "yes":
        if vehicle_to_remove in vehicles:
            vehicles.remove(vehicle_to_remove)
            write_vehicles(vehicles)
            print('You have removed "' + vehicle_to_remove + '" as an authorized vehicle.')
        else:
            print(vehicle_to_remove + " is not in the list.")
    else:
        print("Action canceled.")

def main_menu():
    while True:
        print('********************************')
        print('AutoCountry Vehicle Finder v0.3')
        print('********************************')
        print('Please Enter the following number below from the menu:')
        print('1. PRINT all Authorized Vehicles')
        print('2. SEARCH for Authorized Vehicle')
        print('3. ADD Authorized Vehicle')
        print('4. DELETE Authorized Vehicle')
        print('5. Exit')

        query = input()

        if query == '1':
            print_vehicles()
        elif query == '2':
            search_vehicle()
        elif query == '3':
            add_vehicle()
        elif query == '4':
            delete_vehicle()
        elif query == '5':
            print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
            break
        else:
            print('Invalid option. Please enter a valid number from the menu.')

if __name__ == "__main__":
    main_menu()
