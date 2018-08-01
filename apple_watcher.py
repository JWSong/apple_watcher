import subprocess
import threading
import urllib.request

from bs4 import BeautifulSoup
from datetime import datetime

pnum = input("전화번호를 입력하세요. (ex. +82-10-1234-5678): ")

def start_checking():
    print("{}\t 확인중.. ".format(datetime.today().isoformat()), end='')
    threading.Timer(60 * 30, start_checking).start()
    with urllib.request.urlopen('https://www.apple.com/kr/shop/buy-mac/macbook-pro/15%ED%98%95') as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        purchase_button = soup.find_all(class_='add-to-cart')[-1].button
        if not 'disabled' in purchase_button.attrs['class']:
            print("구매 가능")
            subprocess.Popen(["sh", "imessages.sh", pnum, "맥북 구매가능"], stdin=subprocess.PIPE)
            raise SystemExit
        else:
            print("구매 불가")

start_checking()
