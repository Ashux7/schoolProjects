# imports
import pandas as pd
from tkinter import * #type: ignore
import tkinter as tk
from datetime import datetime 
# from tkinter import ttk


# window
win = Tk()
win.geometry('500x500')
win.title("Welcome to AP MOTORS")

# form
customername = StringVar() # variable to store data entered.
fathername = StringVar()
emailid = StringVar()
phone = IntVar()
company = StringVar()
model = StringVar()
price = IntVar()
qty = IntVar()
# compny = ['TVS','ROYAL ENFIELD','HERO','YAMAHA']
# tvs = ["TVS Raider 125", "TVS Apache RTR 160", "TVS Ronin", "TVS Apache RR 310", "TVS Ntorq 125"]
# re = ["Royal Enfield Hunter 350", "Royal Enfield Classic 350", "Royal Enfield Bullet 350", "Royal Enfield Meteor 350", "Royal Enfield Interceptor 650"]
# yamaha = ["Yamaha FZ-S", "Yamaha R15", "Yamaha R3", "Yamaha YZF-R15", "Yamaha R7"]
# hero = ["Hero Splendor Plus", "Hero Passion Pro", "Hero HF Deluxe", "Hero Xtreme 160R", "Hero Impulse"]

Label(win, text='Entries with * are mandatory.').place(x=200,y=290) # warning
Label(win,text="Customer Name *").place(x=5,y=10) # customer 
Label(win,text="Father Name * ").place(x=5,y=40)  # father
Label(win,text="Email ID * ").place(x=5,y=70) # email
Label(win,text="Phone Number * ").place(x=5,y=100) # phone
Label(win,text="Company").place(x=5,y=130) # company 
Label(win,text="Model").place(x=5,y=160) # bike model
Label(win,text="Price").place(x=5,y=190) # price
Label(win,text="Quantity").place(x=5,y=220) # qty


Entry(win , width=30,textvariable=customername).place(x=150,y=10) # customer entry
Entry(win , width=30,textvariable=fathername).place(x=150,y=40) # father entry
Entry(win , width=40,textvariable=emailid).place(x=150,y=70) # email entry
Entry(win , width=30,textvariable=phone).place(x=150,y=100) # phone entry

Entry(win , width=30,textvariable=company).place(x=150,y=130) # company entry
Entry(win , width=30,textvariable=model).place(x=150,y=160) # model entry
Entry(win , width=30,textvariable=price).place(x=150,y=190) # price entry 
Entry(win , width=30,textvariable=qty).place(x=150,y=220) # qty entry 


# pandas
def datasend():
    df = pd.read_csv("D:\\ASHU\\codes\\Python\\school\\c12\\project\\newbikes.csv")
    # entries = [customername.get(),fathername.get(),emailid.get(),phone.get(),company.get(),model.get(),price.get()]
    try:
        entrydict={'Customer':customername.get(),'Father':fathername.get(),'Email':emailid.get(),'Phone':phone.get(),'Company':company.get(),'Model':model.get(),'Price':price.get(),'Quantity':qty.get()}
        df.loc[len(df.index)]=entrydict #type: ignore
    except:
        errorwin = Tk()
        Label(errorwin,text='Enter valid Details.').pack()
        Button(errorwin,text='Ok',command=errorwin.destroy).pack()
        errorwin.mainloop()
    # dfnew = pd.DataFrame(entrydict)
    # df = df.add(dfnew)
    df.to_csv("D:\\ASHU\\codes\\Python\\school\\c12\\project\\newbikes.csv", index=False)
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
    Label(billwin, text='{} {}'.format(company.get(),model.get()),font=('Arial',12),height=5,width=50,borderwidth=1,relief='solid',anchor=N).grid(row=6,column=1)
    Label(billwin, text='{}'.format(qty.get()),font=('Arial',12),borderwidth=1,relief='solid',height=5,width=10,anchor=N).grid(row=6,column=2)
    Label(billwin, text='{}'.format(price.get()),font=('Arial',12),borderwidth=1,relief='solid',height=5,width=10,anchor=N).grid(row=6,column=3)
    Label(billwin, text=(price.get()*qty.get()),font=('Arial',12),borderwidth=1,relief='solid',height=5,width=10,anchor=N).grid(row=6,column=4)
    Label(billwin, text='TOTAL AMOUNT',font=('Arial',12),borderwidth=1,relief='solid',height=2,width=71,anchor=CENTER).grid(row=7,column=1,columnspan=3)
    Label(billwin, text=(price.get()*qty.get()),font=('Arial',12),borderwidth=1,relief='solid',height=2,width=10,anchor=CENTER).grid(row=7,column=4)



Button(win , text='BILL', command=new_window).place(x=290,y=250)
Button(win , text='SUBMIT', command=datasend).place(x=150,y=250)


mainloop()