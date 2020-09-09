from errbot import BotPlugin, botcmd

class Showok(BotPlugin):

    @botcmd()  # flags a command
    def showok(self, msg, args):  # a command callable with !tryme
        """ validando comentario3 """
        return (self.echotext("web"))
 
    def echotext(self, args):
        return (args+"valid")
