# imports
import pandas as pd
from tkinter import * #type: ignore
import tkinter as tk
from datetime import datetime 



# window
win = Tk()
win.geometry('700x500')
win.title("Welcome to TVS AP MOTORS")
win.rowconfigure(index=15,weight=1)
win.columnconfigure(index=12,weight=1)

# form
customername = StringVar() # variable to store data entered.
fathername = StringVar()
emailid = StringVar()
phone = StringVar()
model = StringVar()
price = IntVar()
qty = IntVar()


mddict = {"Jupiter110cc": 68998,"NTORQ125CC": 73490,"RR310": 78590,"XL100": 84990,"Raider125": 86990,"Ronin225": 265000}
mdlsavail = ['Jupiter110cc','NTORQ125CC','RR310','XL100','Raider125','Ronin225']
mdlsprice=[68998,73490,78590,84990,86990,265000]

Label(win,text="MODELS AVAILABLE WITH THEIR PRICE").grid(row=1,column=0) # models available
for i in range(6):
        Label(win,text=mdlsavail[i],borderwidth=1,relief='solid',width=26).grid(row=i+1,column=1,columnspan=1)
        Label(win,text=mdlsprice[i],borderwidth=1,relief='solid',width=26).grid(row=i+1,column=2)

Label(win,text="Customer Name *").grid(row=7,column=0) # customer 
Label(win,text="Father Name * ").grid(row=8,column=0)  # father
Label(win,text="Email ID * ").grid(row=9,column=0) # email
Label(win,text="Phone Number * ").grid(row=10,column=0) # phone
Label(win,text="Model").grid(row=11,column=0) # bike model
Label(win,text="Quantity").grid(row=12,column=0) # qty
Label(win, text='Entries with * are mandatory.').grid(row=13,column=0) # warning


Entry(win , width=30,textvariable=customername).grid(row=7,column=1) # customer entry
Entry(win , width=30,textvariable=fathername).grid(row=8,column=1) # father entry
Entry(win , width=30,textvariable=emailid).grid(row=9,column=1) # email entry
Entry(win , width=30,textvariable=phone).grid(row=10,column=1) # phone entry
Entry(win , width=30,textvariable=model).grid(row=11,column=1) # model entry
Entry(win , width=30,textvariable=qty).grid(row=12,column=1) # qty entry 


# pandas
def datasend():
    df = pd.read_csv("D:\\ASHU\\codes\\Python\\school\\c12\\project\\project2.0\\bikepurchaseDB.csv")
    # entries = [customername.get(),fathername.get(),emailid.get(),phone.get(),company.get(),model.get(),price.get()]
    if model.get() in mdlsavail and phone.get().isnumeric() == True:
        entrydict={'Customer':customername.get(),'Father':fathername.get(),'Email':emailid.get(),'Phone':int(phone.get()),'Model':model.get(),'Price':mddict[model.get()],'Quantity':qty.get()}
        df.loc[len(df.index)]=entrydict #type: ignore
    else:
        errorwin = Tk()
        Label(errorwin,text='Enter valid Details.').pack()
        Button(errorwin,text='OK',command=errorwin.destroy).pack()
        errorwin.mainloop()
    # dfnew = pd.DataFrame(entrydict)
    # df = df.add(dfnew)
    df.to_csv("D:\\ASHU\\codes\\Python\\school\\c12\\project\\project2.0\\bikepurchaseDB.csv", index=False)
    print(df)

# vals = [customername,fathername,emailid,phone,company,model,price]
# new window
def new_window():
    billwin = Toplevel(win)
    billwin.columnconfigure(index=5,weight=1)
    billwin.rowconfigure(index=7,weight=1)
    billwin.title('BILL | AP MOTORS')
    Label(billwin, text='       AP MOTORS', font=('Algerian',36)).grid(row=1,column=1,columnspan=3)
    Label(billwin, text='                    XYZ Road, Jankipuram, Lucknow - 226220', font='Arial').grid(row=2,column=1,columnspan=3)
    Label(billwin, text='                    Email - apmotorslko@hotmail.com          Contact - 0522-696969', font='Arial').grid(row=3,column=1,columnspan=3)
    Label(billwin, text='Details of Customer              Date:{} Time:{}         \n Name: {} s/o {} | Email: {}'.format(datetime.now().date(),datetime.now().strftime("%H:%M:%S"),customername.get(),fathername.get(),emailid.get()),font=('Arial',10),borderwidth=1,relief='solid',width=91).grid(row=4,column=1,columnspan=4)
    Label(billwin, text='Description of Goods',font=('Arial',12),borderwidth=1,relief='solid',width=50).grid(row=5,column=1)
    Label(billwin, text='Quantity',font=('Arial',12),borderwidth=1,relief='solid',width=10).grid(row=5,column=2)
    Label(billwin, text='Rate',font=('Arial',12),borderwidth=1,relief='solid',width=10).grid(row=5,column=3)
    Label(billwin, text='Amount',font=('Arial',12),borderwidth=1,relief='solid',width=10).grid(row=5,column=4)
    Label(billwin, text='{} {}'.format('TVS',model.get()),font=('Arial',12),height=5,width=50,borderwidth=1,relief='solid',anchor=N).grid(row=6,column=1)
    Label(billwin, text='{}'.format(qty.get()),font=('Arial',12),borderwidth=1,relief='solid',height=5,width=10,anchor=N).grid(row=6,column=2)
    Label(billwin, text='{}'.format(mddict[model.get()]),font=('Arial',12),borderwidth=1,relief='solid',height=5,width=10,anchor=N).grid(row=6,column=3)
    Label(billwin, text=(mddict[model.get()]*qty.get()),font=('Arial',12),borderwidth=1,relief='solid',height=5,width=10,anchor=N).grid(row=6,column=4)
    Label(billwin, text='TOTAL AMOUNT',font=('Arial',12),borderwidth=1,relief='solid',height=2,width=71,anchor=CENTER).grid(row=7,column=1,columnspan=3)
    Label(billwin, text=(mddict[model.get()]*qty.get()),font=('Arial',12),borderwidth=1,relief='solid',height=2,width=10,anchor=CENTER).grid(row=7,column=4)



Button(win , text='SUBMIT', command=datasend).grid(row=14,column=1)
Button(win , text='BILL', command=new_window).grid(row=14,column=2)


mainloop()
