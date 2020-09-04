from errbot import BotPlugin, botcmd

class Showok(BotPlugin):

    @botcmd()  # flags a command
    def showok(self, msg, args):  # a command callable with !tryme
        """ validando comentario2 """
        return ("plugin")
