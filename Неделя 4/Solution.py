from tempfile import gettempdir
from os.path import join
import os.path


class File():
    count = 0

    def __init__(self, path_to_file):
        self.path = path_to_file
        self.current_position = 0
        File.count += 1
        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def __str__(self):
        return self.path

    def read(self):
        with open(self.path) as f:
            readen = f.read()
        return readen

    def write(self, text):
        with open(self.path, 'w') as f:
            f.write(text)

    def __add__(self, obj):
        name = 'new' + str(File.count)
        text = self.read() + obj.read()
        path = join(gettempdir(), name)
        new_file = File(path)
        new_file.write(text)
        return new_file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.current_position)

            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('EOF')

            self.current_position = f.tell()
            return line