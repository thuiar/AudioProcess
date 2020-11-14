import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
import os
dataset = "D"
# path = "F:\\Raw_npy\\Raw_Audio_data\\"+dataset
path = "C:\\Users\\93710\\Desktop\\MOSI(1 channel)"

for i in os.listdir(path):
    file_wav = path+'\\'+i
    print(file_wav)
    y, sr = librosa.load(file_wav, sr=None)
    print(sr)
    # plt.figure(figsize=(12, 8))
    CQT = librosa.amplitude_to_db(librosa.cqt(y, sr=16000), ref=np.max)
    # plt.subplot(4, 2, 4)
    librosa.display.specshow(CQT)
    fig = plt.gcf()
    fig.set_size_inches(3.0/ 3, 3.0/3)  # dpi = 300, output = 700*700 pixels
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    # path_save = "C:\\Users\\93710\Desktop\\Frequence_picture\\"+dataset
    path_save = "C:\\Users\\93710\\Desktop\\MOSI_CQT"
    name = i.split('.')[0]
    file_save = path_save+"\\"+name+'.jpg'
    fig.savefig(file_save, format='jpg', transparent=True, dpi=300, pad_inches=0)
    # plt.show()
    plt.close()