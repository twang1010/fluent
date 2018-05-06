# standard command pattern
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class OpenCommand(Command):
    def __init__(self, app):
        self.app = app

    def execute(self):
        self.app.open()


class PasteCommand(Command):
    def __init__(self, document):
        self.doc = document

    def execute(self):
        self.doc.insert_text()


class MacroCommamd(Command):
    def __init__(self, cmds):
        self.cmds=list(cmds)

    def execute(self):
        for cmd in self.cmds:
            cmd.execute()