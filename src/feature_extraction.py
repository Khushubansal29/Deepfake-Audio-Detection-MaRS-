import numpy as np
import librosa


def extract_features(file_path):

    audio, sr = librosa.load(file_path, sr=None)

    mfccs = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=13
    )

    mfccs_mean = np.mean(mfccs, axis=1)

    zcr = np.mean(
        librosa.feature.zero_crossing_rate(audio)
    )

    spectral_centroid = np.mean(
        librosa.feature.spectral_centroid(
            y=audio,
            sr=sr
        )
    )

    rms = np.mean(
        librosa.feature.rms(y=audio)
    )

    features = np.hstack([
        mfccs_mean,
        zcr,
        spectral_centroid,
        rms
    ])

    return features