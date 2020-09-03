from errbot import BotPlugin, botcmd

class Showok(BotPlugin):

    @botcmd(split_args_with=' ')  # flags a command
    def showok(self, msg, args):  # a command callable with !tryme
        """ validando comentario2 """
        return ("plugin "+args[1] + " ok"+ args[0])
