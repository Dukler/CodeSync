import os
from datetime import datetime
from FileManager import FileManager

def main():
    fileManager = FileManager("D:/test/1", "D:/test/2")
    fileManager.syncFiles()

if __name__ == "__main__":
    main()