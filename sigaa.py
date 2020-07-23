import pyautogui as rpa
import webbrowser as wb
from tkinter import *
import requests
from bs4 import BeautifulSoup as bs

sigaaPath = 'https://sigaa.upb.edu.co/ssomanager/c/SSB'
loginX = 970
loginY = 726

estudiantesX = 612
estudiantesY = 435

seguimientoX = 520
seguimientoY = 763

calificacionesX = 1223
calificacionesY = 680

periodoX = 534 
periodoY = 426

rpa.FAILSAFE = True
rpa.PAUSE = 5

wb.open(sigaaPath)

rpa.moveTo(loginX, loginY)

rpa.click()

rpa.PAUSE = 0.5

rpa.click(x=estudiantesX, y=estudiantesY)

rpa.click(x=seguimientoX, y=seguimientoY)

rpa.scroll(-250)

rpa.click(x=calificacionesX, y=calificacionesY)

rpa.click(x=periodoX, y=periodoY)

rpa.click(x=536, y=461)

rpa.click(x=104, y=470)

rpa.scroll(-500)

rpa.click(x=97, y=822)

rpa.PAUSE = 0.1

req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = BeautifulSoup(req.text, "lxml")

try:
    while True:
        x, y = rpa.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')