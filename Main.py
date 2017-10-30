from FileManager import FileManager
from kivy.app import App


class HelloWorldApp(App):
    pass

def main():
    fileManager = FileManager("D:/test/1", "D:/test/2")
    fileManager.syncFiles()
    HelloWorldApp().run()

if __name__ == "__main__":
    main()