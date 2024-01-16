
import os
import pathlib

from Imports.Replace import Replace
from Imports.GetFile import GetFile

class NameChange:
    def cleanName(self, convert_music_path, og_file_ext):
        file_list = GetFile().getFileList(convert_music_path, og_file_ext)
        file_names_ext = GetFile().getFileNameExt(file_list)

        for path, name_ext in zip(file_list, file_names_ext):
            new_name = Replace().replace(name_ext)
            folder_path = pathlib.Path(path)
            new_path = f"{folder_path.parents[0]}\{new_name}"
            os.rename(path, new_path)

    def revertName(self, save_music_path, new_file_ext):
        file_list = GetFile().getFileList(save_music_path, new_file_ext)
        file_names_ext = GetFile().getFileNameExt(file_list)

        for path, name_ext in zip(file_list, file_names_ext):
            new_name = Replace().replace_underscore(name_ext)
            folder_path = pathlib.Path(path)
            new_path = f"{str(folder_path.parents[0])}/{new_name}"
            os.rename(path, new_path)