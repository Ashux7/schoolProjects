import pandas as pd
from datetime import datetime

dfSELL = pd.read_csv('tasmaySELL.csv',index_col='MedID')
dfPRC = pd.read_csv('tasmayPRC.csv',index_col='NID')

def tsmyMS():
        print('==================================TASMAY MEDICAL STORE==================================')
        print('''
          1) View Inventory
          2) Purchase Medicine
          3) View Purchase History
          ''')
            
        choice = input('Enter Your Choice.')
        if choice == '1':
            print('==================================INVENTORY==================================')
            print(dfSELL)
            print('==============================================================================')
        elif choice == '2':
            print('==============================PURCHASE MEDICINE===============================')
            name = input("Enter your Name:")
            while name.isalpha() == False:
                print('Enter a valid name')
                name = input("Enter your Name:")
            nID = name[0:3] + str(datetime.now().strftime('%H%M'))
            print(dfSELL)
            net = 0
            n = int(input('Enter number of items to purchase.'))
            idls = []
            mednamels = []
            qtyls = []
            amtls = []
            for i in range(n):
                id = input('Enter MedID: ')
                qty = input('Enter Quantity: ')
                while id not in list(dfSELL.index) or qty.isnumeric() == False:
                    print('Enter Valid Details.')
                    id = input('Enter MedID: ')
                    qty = input('Enter Quantity: ')
                qty=int(qty)
                amt = int(dfSELL.at[id,'Price'])*qty
                net += int(amt)
                idls.append(id)
                mednamels.append(dfSELL.loc[id]['MedName'])
                qtyls.append(qty)
                amtls.append(amt)
                dfPRC.loc[nID+str(i)] = {'MedID':id,'MedName':dfSELL.loc[id]['MedName'],'Quantity':qty,'Amount':amt,'Date':datetime.now().date()} #type:ignore
                dfPRC.to_csv('tasmayPRC.csv')
            print('Thanks for Purchasing.')
            print('===========================================================================')
            billbool = input('Would you like to receive the BILL for the above purchase?(Answer in Y/N): ').lower()
            while billbool not in ['y','yes','n','no'] == True:
                print('Enter a valid choice.')
                billbool = input(('Would you like to receive the BILL for the above purchase?(Answer in Y/N).')).lower()
            if billbool == 'y' or billbool == 'yes':
                print()
                print()
                print('===============================BILL=====================================')
                print('Date & Time: ',datetime.now().date(),datetime.now().strftime('%H:%M:%S'))
                print('========================================================================')
                dfbill = pd.DataFrame({'MedID':idls,'MedName':mednamels,'Quantity':qtyls,'Amount':amtls})
                print(dfbill)
                print('Your total is: ',net)
            elif billbool == 'n' or billbool == 'no':
                print('Thank You')
        elif choice == '3':
            print(dfPRC)
            
        else:
            tsmyMS()
X=1
while X==1:
    tsmyMS()
