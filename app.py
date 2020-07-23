from tkinter import *
from sigaaRPA import sigaaRPA

class App(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.config(width=400, height=255)
    self.createWidgets()

  def createWidgets(self):
    Button(self, text="SigaaBot", command=sigaaRPA).pack()
    Button(self, text="QUIT", command=self.quit).pack()

  def notaSigaa(self):
    print("Notas mi ermano")