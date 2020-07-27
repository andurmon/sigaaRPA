import rpa as r
from mouse import click
from xPaths import XPaths as X

class Sigaa():
  def __init__(self):
    self.state = 1
    self.semester = "202010"
    self.terminateBot = False

  def terminate(self):
    self.terminateBot = True

  def sigaaRPA(self):
    r.init()
    r.timeout(30)

    while(self.state > 0):

      if self.terminateBot:
        r.close()
        break

      elif self.state == 1:
        # use url('your_url') to go to web page, url() returns current URL
        r.url('https://sigaa.upb.edu.co/ssomanager/c/SSB')
        self.state = self.state + 1

      elif self.state == 2:
        # use type() to use the keyboard to write something
        if r.exist(X.username) & r.present(X.username):
          r.type(X.username, '000290164')
          r.type(X.password, 'Tandres1997_')
          self.state = self.state + 1
        else:
          print("Couldn\'t find Username and Password Components")
          self.state = 1

      elif self.state == 3:
        # use click() to click on an UI element or x, y location
        self.state = click(X.login, self.state)

      elif self.state == 4:
        ## hace click en Estudiantes
        self.state = click(X.estudiantes, self.state)

      elif self.state == 5:
        ## Hace click en Seguimiento a la formación
        self.state = click(X.seguimieto, self.state)

      elif self.state == 6:
        ## hace click en Calificaciones parciales
        self.state = click(X.calif, self.state)

      elif self.state == 7:
        ## Selecciona el semestre del cual quiere mirar las notas
        r.select(X.semester, self.semester)
        self.state = self.state + 1

      elif self.state == 8:
        ## se hace click en enviar
        r.click(X.enviar)
        self.state = self.state + 1

      elif self.state == 9:
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
              materia = r.read('//*[@class="datadisplaytable"][1]/tbody/tr[5]/td[2]')
              print(materia)
              r.snap('page', './notas/s'+self.semester+'/'+ materia +'.png')
              # r.table('//table[@class="datadisplaytable"][2]', './csv/table'+str(i-1)+'.csv')
            r.dom('history.back()')

        # use wait() to wait for a number of seconds
        # default wait() is 5 seconds
        r.wait(5)
        self.terminateBot = True
      elif self.state == 10:
        r.dom('history.back()')