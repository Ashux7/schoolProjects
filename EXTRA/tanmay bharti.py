import pandas as pd
from datetime import datetime
df = pd.read_csv('D:\\ASHU\\codes\\Python\\school\\c12\\project\\EXTRA\\tanmay bharti.csv',index_col='ORDERID')
x = 2
while x>1:
    print("-----------------------------------------------------------------------------------------------------")
    print("                                    BHARTI COURIER SERVICES                                     ")
    print("-----------------------------------------------------------------------------------------------------")
    print('''
          1) Apply for a Courier
          2) Search by Order ID
          3) Bill for an Order
          4) Exit
    ''')
    ch = int(input('Choose any of the above option: '))
    if ch == 1:
        oid = input('Enter ORDER ID: ')
        sname = input('Enter SENDER NAME: ')
        rname = input('Enter RECEIVER NAME: ')
        adrs = input('Enter ADDRESS: ')
        date = input('Enter DATE OF ORDER: ')
        item = input('Enter ITEM: ')
        amt = input('Enter AMOUNT: ')
        print("-----------------------------------------------------------------------------------------------------")
        df.loc[oid]={'ORDERID':oid,'SENDER NAME':sname,'RECEIVER NAME':rname,'ADDRESS':adrs,'DATE':date,'ITEM':item,'AMOUNT':amt} 
        df.to_csv('D:\\ASHU\\codes\\Python\\school\\c12\\project\\EXTRA\\tanmay bharti.csv')
        print('Order Saved Successfully!')
        print("-----------------------------------------------------------------------------------------------------")
    elif ch == 2:
        print(df.index)
        sid = input('Enter ORDER ID to search: ')
        if sid in df.index:
            print(df.loc[sid])
        else:
            print('ORDER ID Invalid.')
        print("-----------------------------------------------------------------------------------------------------")
    elif ch == 3:
        print(df.index)
        bid = input('Enter ORDER ID to make Bill: ')
        if bid in df.index:
            print("-----------------------------------------------------------------------------------------------------")
            print("                                                BILL                                                 ")
            print("-----------------------------------------------------------------------------------------------------")
            print(datetime.now())
            print(df.loc[bid])
        else:
            print('Invalid Order ID.')
    elif ch == 4:
        break
print('Thank You')
