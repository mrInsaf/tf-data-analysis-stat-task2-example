import pandas as pd
import numpy as np
from scipy.stats import chi2
from scipy.stats import norm


chat_id = 816831722 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    alpha = 1 - p
    s = np.std(x, ddof=1)
    chi2_lower = chi2.ppf(alpha/2, n-1)
    chi2_upper = chi2.ppf(1-alpha/2, n-1)
    lower = np.sqrt((n-1) * s**2 / chi2_upper)
    upper = np.sqrt((n-1) * s**2 / chi2_lower)
    return (lower, upper)
