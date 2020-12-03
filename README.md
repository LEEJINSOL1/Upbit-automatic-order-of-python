# Upbit-automatic-order-of-python
Upbit automatic order of python

<개요>
◈ 국내1위 가상화폐 거래소 업비트에서 제공하는 API기능을 이용하여 업비트 내에 상장되어있는코인을 매우빠른속도로 매수,매도를 반복적으로
주문을 넣습니다. (단주매매) API는 초당8번의 주문을 넣을수있습니다. 

<작동영상>
https://www.youtube.com/watch?v=giuPsSeB73w&feature=emb_title

<라이브러리>
from upbitpy import Upbitpy
import pyupbit
import requests
#import pyautogui
from tkinter import *
import time
import tkinter as tk

<설명>
access = "본인의 accesskey"  #업비트API페이지에서 accesskey와 secretkey를 발급받아와 문자열에 넣습니다.
secret = "본인의 secretkey" 
upbit = pyupbit.Upbit(access, secret) #업비트 객체생성


1. 업비트가 지원하는 모든 암호화폐 목록을 반환 
pyupbit.get_tickers()

2.최근 체결된 코인가격 불러오기
pyupbit.get_current_price("KRW-BTC") #리턴값(최근체결된코인가격)은 문자형으로 반환되므로 나중에 연산을위해서는 따로 형변환이 필요함

3.매수,매도 호가창 불러오기
pyupbit.get_orderbook(tickers="KRW-BTC")

4.코인,원화 잔고조회
upbit.get_balance(ticker="KRW") #업비트 계정내 원화잔고 조회
upbit.get_balance(ticker="KRW-BTC") #업비트 계정내 비트코인잔고 조회

5. 지정가매수, 지정가매도
print(upbit.buy_limit_order("KRW-XRP", 500, 20)) #500원에 리플20개 매수
print(upbit.sell_limit_order("KRW-XRP", 500, 20)) #500원에 리플20개 매도

6. 시장가매수, 시장가매도
print(upbit.buy_market_order("KRW-XRP", 10000)) #리플 10000원어치 시장가 매수
print(upbit.sell_market_order("KRW-XRP", 30))  #리플 30개 시장가매도

7.지정가매수,지정가매도 주문 취소
upbit.cancel_order('e57a3bc0-0b0b-4540-96f2-f35f19c51e8d') #uuid값을 넘겨주면 됩니다.
