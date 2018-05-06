class Document:
    def __init__(self, name):
        self.name = name

    def insert_text(self):
        print('{} insert text'.format(self.name))
