class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path, 'r') as f:
                line = f.read()
        except FileNotFoundError:
            line = ''

        return line
