AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500' ]

while True:
    print('********************************')
    print('AutoCountry Vehicle Finder v0.1')
    print('********************************')
    print('Please Enter the following number below from the following menu:')
    print(' ')
    print('1. PRINT all Authorized Vehicles')
    print('2. SEARCH for Authorized Vehicle')
    print('3. ADD Authorized Vehicle')
    print('4. DELETE Authorized Vehicle')
    print('5. Exit')


    query = input()

    if query == '1':
        print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
        for AllowedVehicles in AllowedVehiclesList:
            print(AllowedVehicles)
    elif query == '2':
        query2 = input("Please Enter the full Vehicle name: ")
        if query2 in AllowedVehiclesList:
            print(query2 + ' is an authorized vehicle.')
        else: 
            print(query2 + ' is not an authorized vehicle, if you recieved this error please check the spelling and try again')
    elif query == '3':
        query3 = input ("Please Enter the full vehcile name you would like to add: ")
        AllowedVehiclesList.append(query3)
        print('You have added "' + (query3) + '"as and authorized vehicle.')
    elif query == '4':
        query4 = input("Please Enter the full Vehicle name you would like to REMOVE: ")
        query5 = input('Are you sure you would like to remove "' + query4 + '"from the Authorized Vehicles List? ')
        if query5 == "yes":
            AllowedVehiclesList.remove(query4)
            print('You have REMOVED "' + query4 + '"as an authorized vehicle')
    elif query == '5': 
        print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
        break
    else:
        print('Invalid option. Please enter a valid number from the menu.')