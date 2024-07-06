import pandas as pd
import numpy as np
P=0
s=0
lpstr = True
print("-----------------------------------------------------------------------------------------------------")
print ("                                     A.M. BOOK SELLERS                                   ")
print("-----------------------------------------------------------------------------------------------------")
while lpstr == True:
    print ("                                                MAIN MENU                                             ")
    print("-----------------------------------------------------------------------------------------------------")
    print("1: Admin")
    print("2: Purchase Menu")
    print("3: Exit")
    print("-----------------------------------------------------------------------------------------------------")
    ch=input("Enter your choice :")
    print("-----------------------------------------------------------------------------------------------------")
    if(ch=='1'):
        print ("                                                ADMIN MENU                                             ")
        print("-----------------------------------------------------------------------------------------------------")
        print("1: Add a new book")
        print("2: View data")
        print("3: Exit")
        a=input("Enter your choice:")
        if(a=='1'):
            e=input("Enter no. of entry")
            for j in e:
                i=input("Enter Book id:")
                n=input("Enter book name:")
                q=input("Enter qty")
                r=input("Enter price")
                if float(r) == TypeError:
                    r = input('Enter valid Price ')
                r=float(r)
                df=pd.DataFrame({"BOOKID":[i],"BOOK NAME":[n],"QUANTITY":[q],"PRICE":[r]})
                df.to_csv("D:\\ASHU\\codes\\Python\\Admin.csv")  # make only one csv
                print("-------------------------BOOK ADDED SUCCESSFULLY-------------------------")
        if(a=='2'):
            A=pd.read_csv("D:\\ASHU\\codes\\Python\\AM BOOKSELLERS.csv")
            print(A)
        if(a=='3'):
            print("------------------------- Exited Successfully -------------------------")
        if a != '1' and a != '2' and a != '3':
            print('Enter a valid option.')
            ch='1'
    if(ch=='2'):
        print ("                                         PURCHASE MENU                                         ")
        print("                 Available books :             ")
        D=pd.read_csv("D:\\ASHU\\codes\\Python\\AM BOOKSELLERS.csv")
        D=pd.DataFrame(D,index=np.arange(1,(len(D))))
        print(D)
        ID_L=[]
        L_L=[]
        N_L=[]
        P_L=[]
        n=int(input("Enter no of books to be puchased"))
        for m in range(n):
            ID=input("Enter book id:")
            L=input("Enter book name :")
            if L not in list(D.loc['BOOKNAME']):
                print('Enter Valid BookName.')
                L1=input("Enter book name :")
                L=L1
            N=input("Enter qty:")
            if int(N)==TypeError:
                print('Enter valid Quantity.')
                n1 = input("Enter qty:")
                N=n1
            N=int(N)
            if(ID=='E1'):
                P=N*50
                s=s+P
            elif(ID=='B1'):
                P=N*200
                s=s+P
            elif(ID=='C1'):
                P=N*250
                s=s+P
            elif(ID=='M1'):
                P=N*150
                s=s+P
            elif(ID=='P1'):
                P=N*300
                s=s+P
            else:
                print('Enter valid BOOK ID.')
            ID_L.append(ID)
            L_L.append(L)
            N_L.append(N)
            P_L.append(P)
        print()
        print("--------- A.M. BOOK SELLERS --------")
        print("--------------- BILL ---------------")
        q=pd.DataFrame({"BOOKID":ID_L,"BOOKNAME":L_L,"QTY":N_L,"PRICE":P_L})
        print(q)
        print("TOTAL Price:",sum(q.PRICE))
        
        break
    if ch=='3':
        print("------------------------- Exited Successfully -------------------------")
        break
    else :
        lpstr=True