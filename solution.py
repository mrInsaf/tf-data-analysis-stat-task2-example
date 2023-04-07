import pandas as pd
import numpy as np
from scipy.stats import chi2
from scipy.stats import norm


chat_id = 816831722 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    mean = np.mean(x)
    std_dev = np.std(x, ddof=1)
    df = n - 1
    
    lower = df * np.square(std_dev) / chi2.ppf(1 - alpha/2, df)
    upper = df * np.square(std_dev) / chi2.ppf(alpha/2, df)
    
    return (np.sqrt(lower), np.sqrt(upper))
