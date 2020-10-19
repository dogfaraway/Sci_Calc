from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np


def LogisticMap():
    mu = np.arange(2, 4, 0.0001)
    x = 0.2  # 初值
    iters = 1000  # 不进行输出的迭代次数
    last = 1000  # 最后画出结果的迭代次数
    for i in tqdm(range(iters+last)):
        x = mu * x * (1 - x)
        if i >= iters:
            plt.plot(mu, x, ',k', alpha=0.25)  # alpha设置透明度
    plt.show()


LogisticMap()

