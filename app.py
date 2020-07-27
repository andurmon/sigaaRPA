import threading
import sys
from tkinter import Button, Frame
from Sigaa_Rpa import Sigaa

class App(Frame):

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.config(width=400, height=255)
    self.createWidgets()

  def createWidgets(self):
    Button(self, text="SigaaBot", command=self.startBot).pack()
    Button(self, text="Terminate task", command=self.terminateBot).pack()
    Button(self, text="QUIT", command=self.quitApp).pack()

  def startBot(self):
    self.bot = Sigaa()
    botThread = threading.Thread(target=self.bot.sigaaRPA, daemon=True)
    botThread.start()

  def terminateBot(self):
    self.bot.terminate()

  def quitApp(self):
    self.bot.terminate()
    sys.exit()