import os
from datetime import datetime
from File import File
import shutil

class FileManager:
    def __init__(self, workspace, destination):
        self.workspaceFileList = []
        self.destinationFileList = []
        self.workspace = []
        self.addWorkspace(workspace)
        self.destination = destination + os.sep
        self.setFileLists()

    def addWorkspace(self, workspacePath):
        workspace = workspacePath + os.sep
        self.workspace.append(workspace)

    def addFileToList(self, fileList, fileToAdd, path):
        f = File(fileToAdd, path, os.path.getmtime(path+fileToAdd))
        fileList.append(f)

    def getFile(self, name, fileList):
        for f in fileList:
            if f.name == name:
                return f

    def syncFiles(self):
        for f in self.workspaceFileList:
            fileToSync = self.getFile(f.name, self.destinationFileList)
            if f.lastModified > fileToSync.lastModified:
                shutil.copy(f.path, fileToSync.path)

    def getFileLastModifiedTimeStamp(self, filePath):
        time = os.path.getmtime(filePath)
        return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

    def setFileLists(self):
        for workspace in self.workspace:
            for f in os.listdir(workspace):
                if f.endswith(".txt"):
                    self.addFileToList(self.workspaceFileList, f, workspace)

        for f in os.listdir(self.destination):
            if f.endswith(".txt"):
                self.addFileToList(self.destinationFileList, f, self.destination)