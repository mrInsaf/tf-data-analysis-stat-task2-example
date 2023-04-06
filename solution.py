import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import t


chat_id = 816831722 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    distance = np.sqrt(x[:, 0]**2 + x[:, 1]**2)
    alpha = 1 - p
    x_mean = np.mean(distance)
    print('x_mean is ', x_mean)
    s = np.std(distance, ddof=1)
    df = len(distance) - 1

    t_value = t.ppf((1 + alpha) / 2, df)
    a = t.interval(alpha, df, loc=x_mean, scale=s/np.sqrt(p))


    return a
