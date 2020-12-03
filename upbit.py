from upbitpy import Upbitpy
import pyupbit
import requests
#import pyautogui
from tkinter import *
import time
import tkinter as tk




#print(aaa)
#print(aaaa)
#print(pyupbit.get_current_price("KRW-BTC"))

#access = "HaxsrPaoeAyQo4gsPEPxj6hHRbEBqkFah6o5FjRY"          # access key
#secret = "x1ez7VjrxOhscqouCXZLf1IoxTVUmNcWDo2QxBR2"          # secret key

#access = "HaxsrPaoeAyQo4gsPEPxj6hHRbEBqkFah6o5FjRY"          # access key
#secret = "x1ez7VjrxOhscqouCXZLf1IoxTVUmNcWDo2QxBR2"          # secret key
    
#upbit = pyupbit.Upbit(access,secret)

#upbit = pyupbit.Upbit(access, secret)

#MyKRW  = upbit.get_balance(ticker="KRW")

#for i in range(1, 3):
    #print(upbit.buy_market_order("KRW-XRP", 510))
    #print(upbit.sell_market_order("KRW-XRP", 1.5))
price = pyupbit.get_current_price("BTC-XRP")
#print(price)
#print(upbit.get_balances())


#window = tk.TK()
#window.mainloop()

window=Tk()
window.title("auto")
   


window.geometry('600x400+500+400')

window.resizable(False, False)

   

#test_1 = Button(window, text="button1")

#test_1.place(x=50, y=30)

   


def getTextInput():
    
    access = textExample.get("1.0","end")
    secret = textExample2.get("1.0","end")
    upbit = pyupbit.Upbit(access, secret)

    
    
    Coin = textExample3.get("1.0","end")
    Number = textExample4.get("1.0","end")
    IntNumber = int(Number)
    #print(type(IntNumber))
    
  
   # for i in range(1, 3):
       # print(upbit.buy_market_order("KRW-XRP", 520))
        #print(upbit.sell_market_order("KRW-XRP", 1.5)) 
    
    

def startAuto():
    
    access = textExample.get("1.0",tk.END+"-1c")
    secret = textExample2.get("1.0",tk.END+"-1c")
    Coin = textExample3.get("1.0",tk.END+"-1c")
    Number = textExample4.get("1.0",tk.END+"-1c")
    IntNumber = int(Number)

    
   #access = "HaxsrPaoeAyQo4gsPEPxj6hHRbEBqkFah6o5FjRY"          # access key
    #secret = "x1ez7VjrxOhscqouCXZLf1IoxTVUmNcWDo2QxBR2"          # secret key
    upbit = pyupbit.Upbit(access,secret)

    price = pyupbit.get_current_price(Coin)
    minprice = 510/price
    print(minprice)
    #print(upbit.sell_market_order(Coin,minprice))
    for i in range(1, IntNumber+1):
       print(upbit.buy_market_order(Coin, 520))
       print(upbit.sell_market_order(Coin, minprice))
    
label1 = Label(window,text="Access key 입력 : ")
label1.place(x=0,y=0)

label2 = Label(window, text="Secret key 입력 : ")
label2.place(x=0,y=30)

textExample = tk.Text(window,height=1,width=45)
textExample.pack()
textExample.place(x=110, y=0)

textExample2 = tk.Text(window,height=1,width=45)
textExample2.pack()
textExample2.place(x=110,y=31)

btnRead=tk.Button(window,height=8,width=10 , text="사용방법", command=getTextInput)
btnRead.place(x=500,y=0)


btnStart=tk.Button(window,height=8,width=10 , text="시작", command=startAuto)
btnStart.place(x=500,y=150)

label3 = Label(window,text="코인 입력 : ")
label3.place(x=15,y=60)

label4 = Label(window, text="반복횟수 : ")
label4.place(x=15,y=90)

textExample3 = tk.Text(window,height=1,width=15)
textExample3.pack()
textExample3.place(x=110,y=62)

textExample4 = tk.Text(window,height=1,width=15)
textExample4.pack()
textExample4.place(x=110,y=93)

label5 = Label(window,text="개발자 : ")
label5.place(x=10,y=150)

textExample5 = tk.Text(window,height=1,width=50)
textExample5.pack()
textExample5.place(x=110,y=155)

#textExample5.insert(END,"3Cw8jEa")




label7= Label(window,text="Access key와 Secret key를 절대 타인에게 노출하지마세요")
label7.place(x=150,y=350)

label8 = Label(window,text="개발자 : ")
#label8.pack()
label8.place(x=10,y=186)


textExample6 = tk.Text(window,height=1,width=50)
textExample6.pack()
textExample6.place(x=110,y=187)

window.mainloop()




