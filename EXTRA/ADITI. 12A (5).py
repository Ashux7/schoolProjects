from tkinter import * #type:ignore
from tkinter import ttk
import pandas as pd 
from random import randint
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

         #================================================================================================================
         def iExit():
             iExit=tkinter.messagebox.askyesno("Tours Travel Management System","Confirm if You wanty to exit")
             if iExit > 0:
                 root.destroy()
                 return

         def Recipt():
             self.txtRecipt.delete("1.0",END) 
             x=randint(10853, 500831)
             randomRef = str(x)
             Recipt_Ref.set("Tours Travel Bill: " + randomRef)

             self.txtRecipt.insert(END,'REcipt Ref:\t\t\t\t\t'+ REcipt_Ref.get() , "\n")
             self.txtRecipt.insert(END,'REcipt Ref:\t\t\t\t\t'+ REcipt_Ref.get() , "\n")
             self.txtRecipt.insert(END,'REcipt Ref:\t\t\t\t\t'+ REcipt_Ref.get() , "\n")
             self.txtRecipt.insert(END,'REcipt Ref:\t\t\t\t\t'+ REcipt_Ref.get() , "\n")
             self.txtRecipt.insert(END,'REcipt Ref:\t\t\t\t\t'+ REcipt_Ref.get() , "\n")
             self.txtRecipt.insert(END,'REcipt Ref:\t\t\t\t\t'+ REcipt_Ref.get() , "\n")
             

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

         ReceiptFrame=LabelFrame(Receipt_ButtonFrame, width=350, height=300, 
                                 font=('arial',12,'bold'), text='Receipt', relief=RIDGE)
         ReceiptFrame.grid(row=0,column=0)

         ButtonFrame=LabelFrame(Receipt_ButtonFrame, width=350, height=100, relief=RIDGE)
                               
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

         self.cboDeparture = ttk.Combobox(TravelFrame, textvariable = var11, state='readonly', font=('arial',20,'bold'),width=14)
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
         self.txAirportTax = Entry(TravelFrame,text = 0,font=('arial',14,'bold'),textvariable=AirportTax, bd=7,
                                   insertwidth=2, justify=RIGHT) 
         self.txAirportTax.grid(row=3,column=1)

         self.txMile=Checkbutton(TravelFrame, text="Air Mile", variable = var2, onvalue= 1, offvalue=0,
                             font=('arial',16,'bold')).grid(row=4, column=0, sticky=W)
         self.txtMile = Entry(TravelFrame,text = 0,font=('arial',14,'bold'),textvariable=Mile, bd=7,
                              insertwidth=2, justify=RIGHT)
         self.txtMile.grid(row=4,column=1)

         self.chkTravelling_Insurance = Checkbutton(TravelFrame, text="Travelling Insurance", variable = var3, onvalue=1,
                                                    offvalue=0,
                                                    font=('arial',16,'bold')).grid(row=5, column=0, sticky=W)

         self.txtTravelling_Insurance = Entry(TravelFrame,text = 0, font=('arial',14,'bold'), textvariable=Travel_Ins, bd=7,
                                              insertwidth=2, justify=RIGHT)
         self.txtTravelling_Insurance.grid(row=5,column=1)

         self.chkExt_Luggage = Checkbutton(TravelFrame, text="Ext. Luggage", variable = var4, onvalue=1, offvalue=0,
                                           font=('arial',16,'bold')).grid(row=6,column=0, sticky=W)
         self.chkExt_Luggage = Entry(TravelFrame,text = 0,font=('arial',14,'bold'), textvariable=Luggage, bd=7,
                                     insertwidth=2, justify=RIGHT)
         self.chkExt_Luggage.grid(row=6,column=1)
         #===================================================================================================================================                               
         def Datasend():
                df = pd.read_csv('D:\\ASHU\\codes\\Python\\school\\c12\\project\\EXTRA\\aditi raj.csv')
                df.loc[len(df.index)]={'Firstname':Firstname.get(),'Surname':Surname.get(),'Address':Address.get(),'PostCode':PostCode.get(),'Telephone':Telephone.get(),'Mobile':Mobile.get(),'Email':Email.get(),'Departure':var11.get(),'Destination':var12.get(),'Accomodation':var13.get(),'AirportTax':AirporTax.get(),'AirMile':Mile.get(),'TravellingInsurance':Travel_Ins.get(),'ExtLuggage':Luggage.get()} # type:ignore
                df.to_csv('D:\\ASHU\\codes\\Python\\school\\c12\\project\\EXTRA\\aditi raj.csv',index=False) 
                print(df)
##################################################################################
         def Bill():
             self.subbtn = Button(ButtonFrame , text='SUBMIT',command = Datasend).grid(row=1,column=0)
         self.billbtn = Button(ButtonFrame, text='Bill',command = Bill).grid(row=1 ,column=1)
###################################################################################
          #=====================================================================================================================================
         self.chKStandard = Checkbutton(Ticket_Frame, text="Standard", variable = var5, onvalue=1, offvalue=0,
                                         font=('arial',14,'bold')).grid(row=0, column=0)
         self.txtStandard = Entry(Ticket_Frame, font=('arial',14,'bold'),width=6, textvariable=Standard, bd=5,
                                   state=DISABLED, justify=RIGHT)
         self.txtStandard.grid(row=0,column=1)

         self.chkSingle = Checkbutton(Ticket_Frame, text="Single", variable = var6, onvalue=1, offvalue=0,
                                       font=('arial',14,'bold')).grid(row=0, column=2, sticky=W)

         self.chkEconomy = Checkbutton(Ticket_Frame, text="Economy", variable = var7, onvalue=1, offvalue=0,
                                        font=('arial',14,'bold')).grid(row=1, column=0, sticky=W)

         self.txtEconomy= Entry(Ticket_Frame,font=('arial',14,'bold'),width=6, textvariable=Economy, bd=5,
                                 state=DISABLED, justify=RIGHT)
         self.txtEconomy.grid(row=1, column=1)

         self.chKReturn = Checkbutton(Ticket_Frame, text="Return", variable = var8, onvalue = 1, offvalue=0,
                                           font=('arial',14,'bold')).grid(row=1, column=2, sticky=W)
          
         self.chKFirstClass = Checkbutton(Ticket_Frame, text="FirstClass", variable = var9, onvalue=1, offvalue=0,
                                         font=('arial',14,'bold')).grid(row=2, column=0)
         self.txtFirstClass = Entry(Ticket_Frame, font=('arial',14,'bold'),width=6, textvariable=Standard, bd=5,
                                   state=DISABLED, justify=RIGHT)
         self.txtFirstClass.grid(row=2,column=1)

         self.chKSpecialNeeds = Checkbutton(Ticket_Frame, text="SpecialNeeds", variable = var8, onvalue = 1, offvalue=0,
                                           font=('arial',14,'bold')).grid(row=2, column=2, sticky=W)

          #=================================================================================================================

        #  self.txtRecipt=Text(ReciptFRame, width=60, height=21,font=('arial',10,'bold'))
        #  self.txtRecipt.grid(row=0, column=0)
          #=================================================================================================================
         self.btnTotal=Button(ButtonFrame, padx=18, bd=7,font=('arial',16,'bold'),width=4,
                               text='Total').grid(row=0, column=0)
          
         self.btnRecipt=Button(ButtonFrame, padx=18, bd=7,font=('arial',16,'bold'),width=4,
                               text='Recipt').grid(row=0, column=1)

         self.btnReset=Button(ButtonFrame, padx=18, bd=7,font=('arial',16,'bold'),width=4,
                            text='Reset').grid(row=0, column=2)
          
         self.btnExit=Button(ButtonFrame, padx=18, bd=7,font=('arial',16,'bold'),width=4,
                               text='Exit', command=iExit).grid(row=0, column=3) 




  
if __name__=='__main__':
    root=Tk()
    application = Travel (root)
    root.mainloop()
    
