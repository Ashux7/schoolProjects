import pandas as pd
df = pd.read_csv('D:\\ASHU\\codes\\Python\\school\\c12\\project\\EXTRA\\prakhyat_anirudh_fitnesscentre.csv',index_col=0)
net = 0
x = 7
while x>1:
    print("-----------------------------------------------------------------------------------------------------")
    print ("                                        A.P. FITNESS CENTRE                                         ")
    print("-----------------------------------------------------------------------------------------------------")
    print('''
          1) View Inventory
          2) Purchase Item
          3) Exit
    ''')
    ch = int(input('Choose any of the above option: '))
    if ch == 1:
        print(df)
    elif ch == 2:
        print(df)
        print("-----------------------------------------------------------------------------------------------------")
        print("                                             PURCHASE ITEMS                                          ")
        print("-----------------------------------------------------------------------------------------------------")
        itemls = []
        qtyls = []
        amtls=[]
        prc = int(input('Enter number of different items to purchase: '))
        for i in range(prc):
            eid = input('Enter item ID: ')
            itemls.append(eid)
            qty = int(input('Enter quantity: '))
            qtyls.append(qty)
            amt = df.loc[eid]['Rate']
            amtls.append(amt)
            net +=amt*qty
        bill = input('Do you want the bill to be displayed? Answer in Y/N: ').lower()
        if bill == 'y':
            print("-----------------------------------------------------------------------------------------------------")
            print("                                                BILL                                                 ")
            print("-----------------------------------------------------------------------------------------------------")
            billdf = pd.DataFrame({'ITEMS':itemls,'QUANTITY':qtyls,'AMOUNT':amtls})
            print(billdf)
            print('Your total would be: ',net)
    elif ch == 3:
        break
print('Thank You')
