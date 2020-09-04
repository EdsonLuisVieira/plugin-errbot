from errbot import BotPlugin, botcmd


class Validate(BotPlugin):
    """
    validate update
    """

    @botcmd  # flags a command
    def validate(self, msg, args):  # a command callable with !tryme
        """
        validate update
        """
        return 'validate pae'  # This string format is markdown.
