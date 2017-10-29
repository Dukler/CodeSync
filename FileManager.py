import os
from datetime import datetime
from File import File
import shutil

class FileManager:
    def __init__(self,workspace,destination):
        self.workspaceFileList=[]
        self.destinationFileList = []
        self.workspace = workspace + os.sep
        self.destination = destination + os.sep
        for file in os.listdir(workspace):
            if file.endswith(".txt"):
                self.addFileToList(self.workspaceFileList, file, self.workspace)
        for file in os.listdir(destination):
            if file.endswith(".txt"):
                self.addFileToList(self.destinationFileList, file, self.destination)

    def addWorkspace(self, worskpacePath):
        self.workspace.append(worskpacePath)

    def addFileToList(self,list,fileToAdd, path):
        file = File(fileToAdd, path, os.path.getmtime(path+fileToAdd))
        list.append(file)

    def getFile(self, name, fileList):
        for file in fileList:
            if file.name == name:
                return file

    def syncFiles(self):
        for file in self.workspaceFileList:
            fileToSync = self.getFile(file.name, self.destinationFileList)
            if file.getDate() > fileToSync.getDate():
                shutil.copy(file.path, fileToSync.path)

    def getFileLastModifiedTimeStamp(self, filePath):
        time = os.path.getmtime(filePath)
        return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')