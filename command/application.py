class Application:
    def __init__(self, name):
        self.name = name

    def open(self):
        print('opening application{}'.format(self.name))
