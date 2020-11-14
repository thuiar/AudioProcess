import librosa
import os
from pydub import AudioSegment
AudioSegment.converter = "D:\\Workspace\\Keras\\keras\\distribute\\ffmpeg-4.1-h6538335_1002\\Library\\bin\\ffmpeg.exe"
path2 = 'C:\\Users\\93710\\Desktop\\MOSI'

path = r'C:\Users\93710\Desktop\MOSI_8K'
for file in os.listdir(path2):
    path_audio = path2 + '\\'+ file
    path1 = path+'\\'+file
    audio = AudioSegment.from_file(path_audio, format("wav"))
    mono = audio.set_frame_rate(8000)
    mono.export(path1, format='wav')
    # y, sr = librosa.load(path1, sr=None)


