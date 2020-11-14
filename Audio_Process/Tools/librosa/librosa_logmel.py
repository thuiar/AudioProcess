import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
import os
def get_spectrograms(fpath, use_path=True):
    '''Returns normalized log(melspectrogram) and log(magnitude) from `sound_file`.
    Args:
      sound_file: A string. The full path of a sound file.
    Returns:
      mel: A 2d array of shape (T, n_mels) <- Transposed
      mag: A 2d array of shape (T, 1+n_fft/2) <- Transposed
    '''

    # Loading sound file
    if use_path:
        y, sr = librosa.load(fpath, sr=16000)
        # with open("x.bin", 'wb') as fp:
        #     for i in range(len(y)):
        #         print("y[", i, "]: ", y[i])
        #         bs = struct.pack("f", y[i])
        #         # a = struct.pack('B', i)
        #         fp.write(bs)
    else:
        y, sr = fpath, 16000
    print("y.shape: ", y.shape)
    print("sr: ", sr)

    # Trimming
    # y, _ = librosa.effects.trim(y)

    # Preemphasis pre-emphasis，预加重
    y = np.append(y[0], y[1:] - 0.97 * y[:-1])

    # stftz
    linear = librosa.stft(y=y,
                          n_fft=2048,
                          hop_length=int(16000 * 0.05),
                          win_length=int(16000 * 0.1))
    # magnitude spectrogram
    mag = np.abs(linear)  # (1+n_fft//2, T)
    # mel spectrogram
    mel_basis = librosa.filters.mel(16000, 2048, 80)  # (n_mels, 1+n_fft//2)

    mel = np.dot(mel_basis, mag)  # (n_mels, t)

    # to decibel
    mel = 20 * np.log10(np.maximum(1e-5, mel))
    mag = 20 * np.log10(np.maximum(1e-5, mag))

    # normalize
    mel = np.clip((mel - 20 + 100) / 100, 1e-8, 1)
    mag = np.clip((mag - 20 + 100) / 100, 1e-8, 1)

    # Transpose
    mel = mel.T.astype(np.float32)  # (T, n_mels)
    mag = mag.T.astype(np.float32)  # (T, 1+n_fft//2)

    #
    mel = mel[:len(mel) // hp.r * hp.r].reshape([len(mel) // hp.r, hp.r * hp.n_mels])
    mag = mag[:len(mag) // hp.r * hp.r]  # .reshape([len(mag)//hp.r,hp.r*1025])


    return mel, mag
