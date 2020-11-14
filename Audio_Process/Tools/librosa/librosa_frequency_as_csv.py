import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
import os
import shutil
import xlrd
import tqdm
# workbook= xlrd.open_workbook('E_Y.xlsx')
# sheets = workbook.sheet_names()
# table = workbook.sheets()[0]
for i in range(2199):
    aaa = 1+i
    name = str(aaa)+'.wav'
    path_csv = "C:\\Users\\93710\\Desktop\\MOSI"
    file_wav = path_csv + '\\' + name
    y, sr = librosa.load(file_wav, sr=None)
    print(sr)
    # plt.figure(figsize=(12, 8))
    CQT = librosa.amplitude_to_db(librosa.cqt(y, sr=16000), ref=np.max)
    # plt.subplot(4, 2, 4)
    librosa.display.specshow(CQT)
    fig = plt.gcf()
    fig.set_size_inches(4.0 / 3, 3.0 / 3)  # dpi = 300, output = 700*700 pixels
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    # path_save = "C:\\Users\\93710\Desktop\\Frequence_picture\\"+dataset
    path_save = "C:\\Users\\93710\\Desktop\\MOSI_picture"
    file_save = path_save + "\\" + str(aaa) + '.jpg'
    fig.savefig(file_save, format='jpg', transparent=True, dpi=300, pad_inches=0)
    # plt.show()
    plt.close()

