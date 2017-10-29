import os

class File:
    def __init__(self, name, path, lastModified):
        self.name = name
        self.path = path
        self.fullName = os.path.join(path, name)
        self.lastModified = lastModified
