import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 816831722 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    # Устанавливаем количество бутстрэп-выборок
    n_bootstrap_samples = 1000
    
    n = len(x)
    bootstrapped_statistics = []
    for i in range(n_bootstrap_samples):
        bootstrap_sample = np.random.choice(x, n, replace=True)
        bootstrapped_statistics.append(np.mean(bootstrap_sample))
    alpha = (1 - p) / 2
    lower_quantile = np.quantile(bootstrapped_statistics, alpha)
    upper_quantile = np.quantile(bootstrapped_statistics, 1 - alpha)
    return lower_quantile, upper_quantile
