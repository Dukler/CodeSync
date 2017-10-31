import os
from Tkinter import *
import tkFileDialog



def main():
    def on_entry_click(event):
        if e.get() == '':
            currdir = os.getcwd()
            tempdir = tkFileDialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
            if len(tempdir) > 0:
                e.insert(0, tempdir)

    #fileManager = FileManager("D:/test/1", "D:/test/2")
    #fileManager.syncFiles()
    root = Tk()
    root.minsize(width=800, height=600)

    e = Entry(root)
    # root.withdraw()  # use to hide tkinter window
    e.pack()
    e.bind("<Button-1>", on_entry_click)
    root.mainloop()

if __name__ == "__main__":
    main()