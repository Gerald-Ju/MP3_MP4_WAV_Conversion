import glob
from pathlib import Path

class GetFile:
    def getFileList(self, path, file_ext):
        return list(glob.glob(f"{path}/*{file_ext}"))

    def getFileNameExt(self, file_list):
        file_names_ext = []
        for file in file_list:
            file_names_ext.append(Path(file).name)
        return file_names_ext

    def getFileName(self, file_list):
        file_names = []
        for file in file_list:
            file_names.append(Path(file).stem)
        return file_names