import application
import command
import document


class Menu:
    def __init__(self, cmds):
        self.cmds = dict(cmds)

    def menu_selected(self, cmd_name):
        self.cmds[cmd_name].execute()


#test

myApp = application.Application("myApp")
myDoc = document.Document("myDoc")

cmds = {'open': command.OpenCommand(myApp),
        'paste': command.PasteCommand(myDoc),
        'macro': command.MacroCommamd([command.OpenCommand(myApp), command.PasteCommand(myDoc)])
        }

menu = Menu(cmds)
menu.menu_selected('open')
menu.menu_selected('paste')
menu.menu_selected('macro')
