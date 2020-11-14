import matplotlib.pyplot as plt
import numpy as np
import librosa.display
import os
file_path = 'C:\\Users\\93710\\Desktop\\Audio\\cats.txt'
label = open(file_path,'rb')
label_ = label.readlines()
for i in range(len(label_)):
    line_ = label_[i]
    line_ = str(line_)
    label_s = line_.split('\\t')[1]
    name_s = line_.split('\\t')[0]
    print(name_s[2:])
    file_wav = 'C:\\Users\\93710\\Desktop\\MOUD(1 channel)\\' + name_s[2:] + '.wav'
    y, sr = librosa.load(file_wav, sr=None)
    S_dB = librosa.feature.melspectrogram(y, sr, n_fft=1024, hop_length=512, n_mels=128)
    # plt.subplot(4, 2, 4)
    # librosa.display.specshow(CQT)
    librosa.display.specshow(librosa.power_to_db(S_dB, ref=np.max))
    fig = plt.gcf()
    fig.set_size_inches(3.0 / 3, 3.0 / 3)  # dpi = 300, output = 700*700 pixels
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    # path_save = "C:\\Users\\93710\Desktop\\Frequence_picture\\"+dataset
    path_save = "C:\\Users\\93710\\Desktop\\MOUD_mel"
    file_save = path_save + "\\" + name_s[2:] + '.jpg'
    fig.savefig(file_save, format='jpg', transparent=True, dpi=300, pad_inches=0)
    # plt.show()
    plt.close()

