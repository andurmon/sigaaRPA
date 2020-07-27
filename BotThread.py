import threading
import sys
from Sigaa_Rpa import Sigaa


class BotThread:
  
  bot = Sigaa()

  def __init__(self, name):
    threading.Thread.__init__(self)
    self.name = name
    self.target = self.bot.sigaaRPA