import numpy as np
import matplotlib.pyplot as plt


def bandpass_filter(x, freq, frequency_of_signal=5, band=0.05):
    if (frequency_of_signal - band) < abs(freq) < (frequency_of_signal + band):
        return x
    else:
        return 0


def detect_outlier_position_by_fft(signal, threshold_freq=1, frequency_amplitude=.01):
    fft_of_signal = np.fft.fft(signal)
    outlier = np.max(signal) if abs(np.max(signal)) > abs(np.min(signal)) else np.min(signal)
    if np.any(np.abs(fft_of_signal[threshold_freq:]) > frequency_amplitude):
        index_of_outlier = np.where(signal == outlier)
        return index_of_outlier[0]
    else:
        return None


def detect_by_fft(data, window=100):
    """
    Detecting outliers by fft.

    Args:
        data:the time series data list
        window:the size of window

    Returns:
        outlier_positions:outliers' positions.
    """
    outlier_positions = []
    for ii in range(window, len(data), window):
        outlier_position = detect_outlier_position_by_fft(data[ii - window:ii + window])
        if outlier_position is not None:
            outlier_positions.append(ii + outlier_position[0] - window)
    return list(set(outlier_positions))


if __name__ == '__main__':
    with open('../data/data.txt') as f:
        datas = [float(c.strip()) for c in f.readlines()]
        plt.figure(1)
        outlier_positions = detect_by_fft(datas, 200)
        plt.scatter(range(len(datas)), datas)
        plt.scatter(outlier_positions, np.array(datas)[outlier_positions])
        plt.legend()
        plt.show()
