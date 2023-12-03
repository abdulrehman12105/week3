while True:
    print('Student id: 19i316')
    print('Press 1 to display the bill of slab 1 and slab2 !')
    print('Press 2 to display the bill of slab3 !')
    print('Press any key to exit !')
    sourceData = [[55,65,75],[120,150,170],[210,230,240]]
    def costSlab1():
        print('----------------------------------------')
        print('Bill for slab 1 is:')
        for x in range(3):
            bill1 = 10*sourceData[0][x]
            print(bill1)
    def costSlab2():
        print('----------------------------------------')
        print('Bill for slab 2 is:')
        for x in range(3):
            bill2 = 15 * sourceData[1][x]
            print(bill2)
    def costSlab3():
        print('----------------------------------------')
        print('Bill for slab 3 is:')
        for x in range(3):
            bill3 = 20 * sourceData[2][x]
            print(bill3)
    choice = input('Enter your choice: ')
    if choice=='1':
        costSlab1()
        costSlab2()
    elif choice == '2':
        costSlab3()
    else:
        exit()
