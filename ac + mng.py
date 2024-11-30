AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

while True:
    print('********************************')
    print('AutoCountry Vehicle Finder v0.1')
    print('********************************')

    print('Please Enter the following number below from the following menu:')
    print(' ')
    print('1. PRINT all Authorized Vehicles')
    print('2. SEARCH for Authorized Vehicle')
    print('3. ADD Authorized Vehicle')
    print('4. Exit')


    query = input()

    if int(query) == 1:
        print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
        for AllowedVehicles in AllowedVehiclesList:
            print(AllowedVehicles)
    if int(query) == 2:
        query2 = input("Please Enter the full Vehicle name: ")
        if query2 in AllowedVehiclesList:
            print(query2 + ' is an authorized vehicle.')
        else: 
            print(query2 + ' is not an authorized vehicle, if you recieved this error please check the spelling and try again')
    if int(query) == 3:
        query3 = input ("Please Enter the full vehcile name you would like to add: ")
        AllowedVehiclesList.append(query3)
        print('You have added "' + (query3) + '"as and authorized vehicle.')
    if int(query) == 4: 
        print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')