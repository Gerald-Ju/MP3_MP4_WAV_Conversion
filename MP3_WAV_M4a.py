import os

from Imports.AskFolderLoc import AskFolderLoc
from Imports.AskFileExt import AskFileExt
from Imports.ConvertAudio import ConvertAudio
from Imports.NameChange import NameChange
from Imports.GetFile import GetFile

def main():
    convert_music_path = AskFolderLoc().askAudioLoc()
    save_music_path = AskFolderLoc().askSaveMusicLoc()
    og_file_ext, new_file_ext = AskFileExt().askExt()
    NameChange().cleanName(convert_music_path, og_file_ext)

    file_list = GetFile().getFileList(convert_music_path, og_file_ext)
    file_names = GetFile().getFileName(file_list)

    os.chdir(save_music_path)
    ConvertAudio(file_list, file_names, og_file_ext, new_file_ext).options()
    
    NameChange().revertName(save_music_path, new_file_ext)
    NameChange().revertName(convert_music_path, og_file_ext)

    print("\n--------------------------------------------------------\n")
    print("\n                      COMPLETE\n")
    print("\n--------------------------------------------------------\n")

if __name__=="__main__":
    main()