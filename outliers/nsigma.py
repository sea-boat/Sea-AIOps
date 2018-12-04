import numpy as np
import matplotlib.pyplot as plt


def detect_by_nsigma(data, n_sigma=3):
    """
        Detecting outliers by n sigma.

        Args:
            data:the time series data list
            n_sigma:the number of sigma

        Returns:
            outlier_positions:outliers' positions.
        """
    mu = np.mean(data)
    sigma = np.std(data)
    marker_indexs = []
    for i, c in enumerate(data):
        if c > (mu + n_sigma * sigma) or c < (mu - n_sigma * sigma):
            marker_indexs.append(i)
    return marker_indexs


if __name__ == '__main__':
    with open('../data/data.txt') as f:
        datas = [float(c.strip()) for c in f.readlines()]
        plt.figure(1)
        outlier_positions = detect_by_nsigma(datas, 3)
        plt.scatter(range(len(datas)), datas)
        plt.scatter(outlier_positions, np.array(datas)[outlier_positions])
        plt.legend()
        plt.show()
