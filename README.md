
# Convert between MP3, M4A and WAV Audio Files

Just a fun side project that was made because apparently Itunes doesn't support adding MP3 audio files anymore. I was wondering why my .mp3 files kept diverting to the "Not Added" folder. 

Originally made to convert MP3 to M4A to solve the problem but added WAV because why not. 

Can technically be used for all FFmpeg supported files. Fiddling with the code for that is required.

## Uses pure Python (3.10.1) and FFmpeg. 
https://ffmpeg.org/download.html
(add FFmpeg to PATH).

Alternatively you can just download FFmpeg and add an absolute path to the code.

e.g. From this:
```
def MP3toM4A(self):
        for file, name in zip(self.file_list, self.file_names):    
            subprocess.run(f"ffmpeg -i {file} -c:a aac -b:a 192k {name}.{self.new_file_ext}")
```

To this:

```
ffmpeg = r"C:\Users\Gerald Ju\ffmpeg-6.0-essentials_build\bin\ffmpeg.exe"

def MP3toM4A(self):
        for file, name in zip(self.file_list, self.file_names):    
            subprocess.run(f"{ffmpeg} -i {file} -c:a aac -b:a 192k {name}.{self.new_file_ext}")
```
Don't forget to add the curly braces around ffmpeg.



## How to use

To run the program, open a terminal and follow the prompts. 

e.g.
```
C:\Users\Gerald\ConvertAudio> python MP3_WAV_M4a.py
```