import time
from pathlib import Path
from tkinter.filedialog import askdirectory

class AskFolderLoc:
    def askSaveMusicLoc(self):
        print("\nChoose a Folder to Save Music\n")
        time.sleep(1)
        save_music_path = rf"{askdirectory(title='Save Music Folder')}"
        
        return save_music_path

    def askAudioLoc(self):
        print("\nChoose Folder with Music to Convert\n")
        time.sleep(1)
        convert_music_path = rf"{askdirectory(title='Music to Convert Folder')}"
        
        return convert_music_path