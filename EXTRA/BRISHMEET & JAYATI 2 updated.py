def hasNumbers(inputString):
  return any(char.isdigit() for char in inputString)
print("=========================DATABASE==========================================")
import pandas as pd
s=pd.read_csv("C:\\Users\student\Desktop\csv sheet.csv")
print (s)
print("=============================================================================================================================================================BOOK YOUR SHOW=======================================================================================================================================================================================")
namesList = []
while True:
  name = input("Please enter your name,and type done in next line if finished entering your name : \n")
  if hasNumbers(name):
    print ("INVALID INPUT,TRY AGAIN!")
  else:
    if name == "done" or name == "DONE" or name == "Done":
      print("There are", len(namesList), "names in the list", namesList)
      break
    else:
      namesList.append(name)
      
def t_movie():
    print("Movies Running-:")
    print("1.oppenheimer")
    print("2.IT")
    print("3.intersteller")
    movie = int(input("choose your movie: "))
    if movie == 1 :
      theater()
    elif movie == 2:
      theater()
    elif movie == 3:
      theater()
    else:
      print ("Wrong choice")

def theater():
    print("which screen do you want to watch movie: ")
    print("1. SCREEN 1")
    print("2. SCREEN 2")
    print("3. SCREEN 3")
    print("4. SCREEN 4")
    print("5. SCREEN 5")
    a= int(input("choose your screen: "))
    if (a==1):
      seat()
    elif (a==2):
      seat()
    elif (a==3):
      seat()
    elif (a==4):
      seat()
    elif (a==5):
      seat()
    else:
      print("wrong choice")
def seat():
    print("Please select your seats:")
    print("a1 a2 a3 a4 a5    a6 a7 a8 a9 a10 a11 a12 a13 a14 a15    a16 a17 a18 a19 a20")
    print("b1 b2 b3 b4 b5    b6 b7 b8 b9 b10 b11 b12 b13 b14 b15    b16 b17 b18 b19 b20")
    print("c1 c2 c3 c4 c5    c6 c7 c8 c9 c10 c11 c12 c13 c14 c15    c16 c17 c18 c19 c20")
    print("d1 d2 d3 d4 d5    d6 d7 d8 d9 d10 d11 d12 d13 d14 d15    d16 d17 d18 d19 d20")
    print("e1 e2 e3 e4 e5    e6 e7 e8 e9 e10 e11 e12 e13 e14 e15    e16 e17 e18 e19 e20")
    print("f1 f2 f3 f4 f5    f6 f7 f8 f9 f10 f11 f12 f13 f14 f15    f16 f17 f18 f19 f20")
    print("g1 g2 g3 g4 g5    g6 g7 g8 g9 g10 g11 g12 g13 g14 g15    g16 g17 g18 g19 g20")
    print("                                                                            ")
    print("                                                                            ")
    print("h1 h2 h3 h4 h5    h6 h7 h8 h9 h10 h11 h12 h13 h14 h15    h16 h17 h18 h19 h20")
    print("i1 i2 i3 i4 i5    i6 i7 i8 i9 i10 i11 i12 i13 i14 i15    i16 i17 i18 i19 i20")
    a=int(input("Enter number of seats:"))
    ls=[]
    for e in range(a):
      f=input("Enter seat number:")
      ls.append(f)
      i=input("Enter l for luxury and n for normal:")
      if i=='l':
         j=500
      elif i=='n':
         j=250
      else:
        print('Wrong input!')
    food()

              
def food():
  print("What would you like to have ? :")
  print("1. Popcorn(coke+nachos)")
  print("2. Burger(french fries+coke)")
  print("3. Samosa(tea+chips)")
  print("4. Pizza(coke+small size popcorn)")
  print("5. Sandwitch(tea+nachos)")
  print("6. Chicken nuggets(coke+french fries)")
  print("7. nachos(coke+fries)")
  print("8. sweetcorn")
  print("9. Bonus combo:(pizza+coke+chicken nuggets+small size fries)")
  a=int(input("order your food:"))
  if (a==1):
    print("Your order is Successfull")
  elif (a==2):
    print("Your order is Successfull")
  elif (a==3):
    print("Your order is Successfull")
  elif (a==4):
    print("Your order is Successfull")
  elif (a==5):
    print("Your order is Successfull")
  elif (a==6):
    print("Your order is Successfull")
  elif (a==7):
    print("Your order is Successfull")
  elif (a==8):
    print("Your order is Successfull")
  elif (a==9):
    print("Your order is Successfull")
  else:
    print("wrong choice")

      
def ticket():
    a=int(input("Number of tickets do you want?:  "))
    timing(a)
def timing(a):
    time1={
        '1': "10.00-1.00",
        '2': "1.00-4.00",
        '3': "4.00-7.00",
        '4': "7.00-9.00"
    }
    time2 = {
        '1': "10.15-1.15",
        '2': "1.25-4.25",
        '3': "4.35-7.35",
        '4': "7.45-10.45"
    }
    time3 = {
        '1': "10.30-1.30",
        '2': "1.40-4.40",
        '3': "4.50-7.50",
        '4': "8.00-10.45"
    }
    if a == 1:
        print("choose your time:")
        print(time1)
        t = input("select tour time:")
        x = time1[t]
        print("successful!, enjoy your movie at " +x)
    elif a == 2:
        print("choose your time:")
        print(time2)
        t = input("select your time:")
        x = time2[t]
        print("successful!, enjoy movie at "+x)
    elif a == 3:
        print("choose your time:")
        print(time3)
        t = input("select your time:")
        x = time3[t]
        print("successful!, enjoy movie at "+x)
    elif a == 4:
        print("choose your time:")
        print(time4)
        t = input("select your time:")
        x = time4[t]
        print("successful!, enjoy movie at "+x)
    
def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("wrong choice")
def center():
    print("which theater do you wish to see movie? ")
    print("1.Inox")
    print("2.Icon")
    print("3.pvp")
    print("4.back")
    a = int(input("choose your option: "))
    movie(a)

def city():
    print("Greetings!Welcome to our site , We wish you have a good time ahead!")
    print("where you want to watch movie?:")
    print("1.LUCKNOW ")
    print("2.KANPUR ")
    print("3.UNNAO ")
    place = int(input("choose your option: "))
    if place == 1:
      center()
    elif place == 2:
      center()
    elif place == 3:
      center()
    else:
      print("wrong choice")
city()
def language():
    print("in which lanuguage do you want to watch movie?:")
    print("1.ENGLISH")
    print("2.HINDI")
    language = int(input("choose your option: "))
    if language == 1 or language == 2:
      pass
    else:
        print("wrong choice")
language()
base_price = 200
child_discount = 0.5
senior_discount = 0.75
surcharge3d = 1.35
type = (input("Is the movie you are seeing in 3D?\n"))
age = eval(input("How old are you?\n"))
if type == 'No' or 'no':
    if age <= 12:
        total = base_price * child_discount
    elif 12 < age < 65:
        total = base_price
    else:
        total = base_price * senior_discount
elif type == 'Yes' or 'yes':
    if age <= 12:
        total = base_price * surcharge3d * child_discount
    elif 12 < age < 65:
        total = base_price * surcharge3d
    else:
        total = base_price * surcharge3d * senior_discount
print("The total cost of your ticket is", round(total, 2), "rupees.")



    
    

        
        

        
        
        
        
    
    
    
    
