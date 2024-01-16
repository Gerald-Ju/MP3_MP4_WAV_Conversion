import subprocess

class ConvertAudio:
    def __init__(self, file_list, file_names, og_file_ext, new_file_ext):
        self.file_list = file_list
        self.file_names = file_names
        self.og_file_ext = og_file_ext
        self.new_file_ext = new_file_ext

    def MP3toM4A(self):
        for file, name in zip(self.file_list, self.file_names):    
            subprocess.run(f"ffmpeg -i {file} -c:a aac -b:a 192k {name}.{self.new_file_ext}")

    def MP3toWAV(self):
        for file, name in zip(self.file_list, self.file_names):    
            subprocess.run(f"ffmpeg -i {file} {name}.{self.new_file_ext}")

    def WAVtoMP3(self):
        for file, name in zip(self.file_list, self.file_names):    
            subprocess.run(f"ffmpeg -i {file} -acodec libmp3lame {name}.{self.new_file_ext}")   

    def WAVtoM4A(self):
        for file, name in zip(self.file_list, self.file_names):    
            subprocess.run(f"ffmpeg -i {file} -c:a aac -b:a 256k {name}.{self.new_file_ext}")   

    def M4AtoMP3(self):
        for file, name in zip(self.file_list, self.file_names):    
            subprocess.run(f"ffmpeg -i {file} -acodec libmp3lame -vn {name}.{self.new_file_ext}")

    def M4AtoWAV(self):
        for file, name in zip(self.file_list, self.file_names):    
            subprocess.run(f"ffmpeg -i {file} {name}.{self.new_file_ext}")

    def options(self):
        # MP3
        if (self.og_file_ext == "mp3") and (self.new_file_ext == "m4a"):
            self.MP3toM4A()
        elif (self.og_file_ext == "mp3") and (self.new_file_ext == "wav"):
            self.MP3toWAV()
        # WAV
        elif (self.og_file_ext == "wav") and (self.new_file_ext == "mp3"):
            self.WAVtoMP3()
        elif (self.og_file_ext == "wav") and (self.new_file_ext == "m4a"):
            self.WAVtoM4A()
        # M4A
        elif (self.og_file_ext == "m4a") and (self.new_file_ext == "wav"):
            self.M4AtoWAV()
        elif (self.og_file_ext == "m4a") and (self.new_file_ext == "mp3"):
            self.M4AtoMP3()
        else:
            print("\nError has occurred\n")


    """
    ogg to mp3
    ffmpeg -i audio.ogg -acodec libmp3lame audio.mp3

    ac3 to mp3
    ffmpeg -i audio.ac3 -acodec libmp3lame audio.mp3

    aac to mp3
    ffmpeg -i audio.aac -acodec libmp3lame audio.mp3
    """