from tkinter import*
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox

class Travel:

     def __init__(self,root):
         self.root = root
         self.root.title("Tours Travel Management System")
         self.root.geometry("1350x750+0+0")
         self.root.configure(background='black')

         DateofOrder=StringVar()
         DateofOrder.set(time.strftime("%d/%m/%y"))
         Recipt_Ref=StringVar()
         PaidTax=StringVar()
         SubTotal=StringVar()
         TotalCost=StringVar()

         var1=IntVar()
         var2=IntVar()
         var3=IntVar()
         var4=IntVar()
         var5=IntVar()
         var6=IntVar()
         var7=IntVar()
         var8=IntVar()
         var9=IntVar()
         var10=IntVar()
         var11=StringVar()
         var12=StringVar()
         var13=StringVar()

         Firstname=StringVar()
         Surname=StringVar()
         Address=StringVar()
         PostCode=StringVar()
         Telephone=StringVar()
         Mobile=StringVar()
         Email=StringVar()
         AirportTax=StringVar()

         AirporTax =StringVar()
         Mile =StringVar()
         Travel_Ins =StringVar()
         Luggage =StringVar()

         Standard=StringVar()
         Economy=StringVar()
         FirstClass=StringVar()

         AirporTax.set("0")
         Mile.set("0") 
         Travel_Ins.set("0") 
         Luggage.set("0")  

         Standard.set("0") 
         Economy.set("0") 
         FirstClass.set("0")

         #=================================================================================================================
         MainFrame=Frame(self.root)
         MainFrame.grid()

         Tops = Frame(MainFrame, bd=20, width=1350, relief=RIDGE)
         Tops.pack(side=TOP)

         self.lbTitle=Label(Tops, font=('arial',60,'bold'),text="Tours Travel Management System")
         self.lbTitle.grid()
         #=================================================================================================================
         CustomerDetailsFrame=Frame(MainFrame, width=1350, height=500, bd=20, pady=5, relief=RIDGE)
         CustomerDetailsFrame.pack(side=BOTTOM)

         FrameDetails=Frame(CustomerDetailsFrame, width=880, height=300, bd=10, relief=RIDGE)
         FrameDetails.pack(side=LEFT)

         CustomerName=LabelFrame(FrameDetails, width=150, height=250, bd=20,
                                 font=('arial',10,'bold'), text='Customer Name', relief=RIDGE)
         CustomerName.grid(row=0,column=0)

         TravelFrame = LabelFrame(FrameDetails, bd=10, width=300, height=250,
                       font=('arial',12,'bold'),text='Travel details',relief=RIDGE)
         TravelFrame.grid(row=0,column=1)

         Ticket_Frame = LabelFrame(FrameDetails, width=300, height=150, relief=FLAT)
         Ticket_Frame.grid(row=1,column=0)

         CostFrame = LabelFrame(FrameDetails, width=150, height=150, relief=FLAT)
         CostFrame.grid(row=1,column=1)
        
         #=================================================================================================================
         Receipt_ButtonFrame=Frame(CustomerDetailsFrame, bd=10, width=450, height=400, relief=RIDGE)
         Receipt_ButtonFrame.pack(side=RIGHT)

         ReceiptFrame=LabelFrame(Receipt_ButtonFrame, width=350, height=300, bd=20,
                                 font=('arial',12,'bold'), text='Receipt', relief=RIDGE)
         ReceiptFrame.grid(row=0,column=0)

         ButtonFrame=LabelFrame(Receipt_ButtonFrame, width=350, height=100, bd=5,
                                 font=('arial',12,'bold'), text='Buttons', relief=RIDGE)
         ButtonFrame.grid(row=1,column=0)
         #=================================================================================================================
         self.lblFirstname=Label(CustomerName, font=('arial',14,'bold'), text="FirstName", bd=7)
         self.lblFirstname.grid(row=0,column=0, sticky=W)
         self.txtFirstname = Entry(CustomerName,font=('arial',14,'bold'), textvariable=Firstname, bd=7,
                                   insertwidth=2, justify=RIGHT)
         self.txtFirstname.grid(row=0,column=1)

         self.lblSurname = Label(CustomerName, font=('arial',14,'bold'), text="SurName", bd=7)
         self.lblSurname.grid(row=1,column=0, sticky=W)
         self.txtSurname = Entry(CustomerName,font=('arial',14,'bold'), textvariable=Surname, bd=7,
                                 insertwidth=2, justify=RIGHT)
         self.txtSurname.grid(row=1,column=1)

         self.lblAddress = Label(CustomerName, font=('arial',14,'bold'), text="Address", bd=7)
         self.lblAddress.grid(row=2,column=0, sticky=W)
         self.txtAddress = Entry(CustomerName,font=('arial',14,'bold'), textvariable=Address, bd=7,
                                 insertwidth=2, justify=RIGHT)
         self.txtAddress.grid(row=2,column=1)

         self.lblPostCode = Label(CustomerName, font=('arial',14,'bold'), text="Post Code", bd=7)
         self.lblPostCode.grid(row=3,column=0, sticky=W)
         self.txtPostCode = Entry(CustomerName,font=('arial',14,'bold'), textvariable=PostCode, bd=7,
                                   insertwidth=2, justify=RIGHT)
         self.txtPostCode.grid(row=3,column=1)

         self.lblTelephone = Label(CustomerName, font=('arial',14,'bold'), text="Telephone", bd=7)
         self.lblTelephone.grid(row=4,column=0, sticky=W)
         self.txtTelephone = Entry(CustomerName,font=('arial',14,'bold'), textvariable=Telephone, bd=7,
                                   insertwidth=2, justify=RIGHT)
         self.txtTelephone.grid(row=4,column=1)

         self.Mobile = Label(CustomerName, font=('arial',14,'bold'), text="Mobile", bd=7)
         self.Mobile.grid(row=5,column=0, sticky=W)
         self.Mobile = Entry(CustomerName,font=('arial',14,'bold'), textvariable=Mobile, bd=7,
                             insertwidth=2, justify=RIGHT)
         self.Mobile.grid(row=5,column=1)

         self.lblEmail = Label(CustomerName,font=('arial',14,'bold'), text="Email", bd=7)
         self.lblEmail.grid(row=6,column=0, sticky=W)
         self.txtEmail = Entry(CustomerName,font=('arial',14,'bold'), textvariable=Email, bd=7,
                               insertwidth=2, justify=RIGHT)
         self.txtEmail.grid(row=6,column=1)
    
         #=================================================================================================================
         self.lbDeparture = Label(TravelFrame,font=('arial',14,'bold'), text="departure", bd=7)
         self.lbDeparture.grid(row=0,column=0, sticky=W)

         self.cboDeparture = ttk.Combobox(TravelFrame, textvariable = var11, state='readonly', font=('arial',20,'bold'),
                                          width=14)
         self.cboDeparture['value']=('','Delhi', 'Gujrat','Karnataka','Maharashtra')
         self.cboDeparture.current(0)
         self.cboDeparture.grid(row=0,column=1)

         self.lbDestination = Label(TravelFrame,font=('arial',14,'bold'), text="Destination", bd=7)
         self.lbDestination.grid(row=1,column=0, sticky=W)

         self.cboDestination = ttk.Combobox(TravelFrame, textvariable = var12, state='readonly', font=('arial',20,'bold'),
                                            width=14)
         self.cboDestination['value']=('','Jaipur','Mumbai','Kashmir','Goa')
         self.cboDestination.current(0)
         self.cboDestination.grid(row=1,column=1)

         self.lbAccommodation = Label(TravelFrame, font=('arial',14,'bold'), text="Accommodation", bd=7)
         self.lbAccommodation.grid(row=2,column=0, sticky=W)

         self.cboAccommodation = ttk.Combobox(TravelFrame, textvariable = var13, state='readonly', font=('arial',20,'bold'),
                                              width=14)
         self.cboAccommodation['value']=('','1','2','3','4')
         self.cboAccommodation.current(1)
         self.cboAccommodation.grid(row=2,column=1)
         
         #=================================================================================================================    
         self.chkAirportTax=Checkbutton(TravelFrame,text="Airport Tax",variable = var1, onvalue=1, offvalue=0,
                                        font=('arial', 16,'bold')).grid(row=3, column=0, sticky=W)
         self.txAirportTax = Entry(TravelFrame,font=('arial',14,'bold'),textvariable=AirportTax, bd=7,
                                   insertwidth=2,state = DISABLED, justify=RIGHT)
         self.txAirportTax.grid(row=3,column=1)

         self.txMile=Checkbutton(TravelFrame, text="Air Mile", variable = var2, onvalue= 1, offvalue=0,
                             font=('arial',16,'bold')).grid(row=4, column=0, sticky=W)
         self.txtMile = Entry(TravelFrame,font=('arial',14,'bold'),textvariable=Mile, bd=7,
                              insertwidth=2,state=DISABLED, justify=RIGHT)
         self.txtMile.grid(row=4,column=1)

         self.chkTravelling_Insurance = Checkbutton(TravelFrame, text="Travelling Insurance", variable = var3, onvalue=1,
                                                    offvalue=0,
                                                    font=('arial',16,'bold')).grid(row=5, column=0, sticky=W)

         self.txtTravelling_Insurance = Entry(TravelFrame, font=('arial',14,'bold'), textvariable=Travel_Ins, bd=7,
                                              insertwidth=2,state=DISABLED, justify=RIGHT)
         self.txtTravelling_Insurance.grid(row=5,column=1)

         self.chkExt_Luggage = Checkbutton(TravelFrame, text="Ext. Luggage", variable = var4, onvalue=1, offvalue=0,
                                           font=('arial',16,'bold')).grid(row=6,column=0, sticky=W)
         self.chkExt_Luggage = Entry(TravelFrame,font=('arial',14,'bold'), textvariable=Luggage, bd=7,
                                     insertwidth=2,state=DISABLED, justify=RIGHT)
         self.chkExt_Luggage.grid(row=6,column=1)
         #===================================================================================================================================                               
         






  
if __name__=='__main__':
    root=Tk()
    application = Travel (root)
    root.mainloop()
    
