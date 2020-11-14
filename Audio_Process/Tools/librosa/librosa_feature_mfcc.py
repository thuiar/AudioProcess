import matplotlib.pyplot as plt
import numpy as np
import pickle
import librosa.display
import os
path = "C:\\Users\\93710\\Desktop\\MOSI_datasets"
mfcc = []
for i in os.listdir(path):
    file_wav = path+'\\'+i
    print(file_wav)
    y, sr = librosa.load(file_wav, sr=None)
    mfcc_ = librosa.feature.mfcc(y=y,n_mfcc=1, sr=sr)
    mfcc.append(len(mfcc_[0]))
mfcc.sort()
print(mfcc)
print(mfcc[int(2199*0.8)])
print(mfcc[int(2199*0.9)])
print(mfcc[2198])
# mfcc1 = np.asarray(mfcc)
# np.save("C:\\Users\\93710\\Desktop\\新建文件夹 (2)\\mosi_mfcc.npy", mfcc)