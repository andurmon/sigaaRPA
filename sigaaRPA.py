import rpa as r
import pandas as pd
from mouse import click
state = 1
usernameX = '//*[@id="username"]'
passwordX = '//*[@id="password"]'
loginX = '//button[@class="login100-form-btn"]'
estudiantesX = '//button[@id="bmenu--P_StuMainMnu___UID2"]'
seguimietoX = '//*[@id="bmenu--P_AdminMnu___UID4"]'
califX = '//*[@id="contentItem22"]'
semestreX = '//*[@id="term_id"]'
enviarX = '//*[@id="id____UID6"]'

r.init()
r.timeout(30)

while(state > 0):
  if state == 1:
    # use url('your_url') to go to web page, url() returns current URL
    r.url('https://sigaa.upb.edu.co/ssomanager/c/SSB')
    state = state + 1

  elif state == 2:
    # use type() to use the keyboard to write something
    if r.exist(usernameX) & r.present(usernameX):
      r.type(usernameX, '000290164')
      r.type(passwordX, 'Tandres1997_')
      state = state + 1
    else:
      print("Couldn\'t find Username and Password Components")
      state = 1

  elif state == 3:
    # use click() to click on an UI element or x, y location
    state = click(loginX, state)

  elif state == 4:
    ## hace click en Estudiantes
    state = click(estudiantesX, state)

  elif state == 5:
    ## Hace click en Seguimiento a la formación
    state = click(seguimietoX, state)

  elif state == 6:
    ## hace click en Calificaciones parciales
    state = click(califX, state)

  elif state == 7:
    ## Selecciona el semestre del cual quiere mirar las notas
    r.select(semestreX, '202010')
    state = state + 1

  elif state == 8:
    ## se hace click en enviar
    r.click(enviarX)
    state = state + 1

  elif state == 9:
    texto = 'jeje'
    tablexpath = ''
    r.wait(2)
    numCursos = r.count('//*[@class="datadisplaytable"][2]/tbody/tr/td/a')
    for i in range(2,numCursos+2):
      tablexpath = '//*[@class="datadisplaytable"][2]/tbody/tr['+ str(i) +']/td/a'
      if r.exist(tablexpath):
        r.click(tablexpath)
        r.wait(1)
        pagetitle = r.read('//div[@id="pagetitle"]')
        if pagetitle == 'Detalle de Calificación de Componente':
          r.snap('page', './notas/materia'+str(i)+'.png')
          r.table('//table[@class="datadisplaytable"][2]', './csv/table'+str(i-1)+'.csv')
        r.dom('history.back()')

    # use wait() to wait for a number of seconds
    # default wait() is 5 seconds
    r.wait(5)
    r.close()
    state = 0
  elif state == 10:
    r.dom('history.back()')