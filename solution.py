import pandas as pd
import numpy as np
from scipy.stats import chi2
from scipy.stats import norm


chat_id = 816831722 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    x_mean = np.mean(x)
    s_squared = np.sum((x - x_mean) ** 2) / (n - 1)

    alpha = 1 - p  # уровень значимости
    df = n - 1    # степень свободы

    chi2_lower = chi2.ppf(alpha / 2, df)
    chi2_upper = chi2.ppf(1 - alpha / 2, df)

    ci_lower = np.sqrt((n - 1) * s_squared / chi2_upper)
    ci_upper = np.sqrt((n - 1) * s_squared / chi2_lower)
    return ci_lower, ci_upper
