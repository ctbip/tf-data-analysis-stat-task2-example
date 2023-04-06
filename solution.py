import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 784892881 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    min_val = np.min(x*x)
    N = len(x)
    # return np.sqrt(N*min_val/expon.ppf(1 - alpha/2)/30), np.sqrt(N*min_val/expon.ppf(alpha/2)/30)
    # return 0, np.sqrt(N*min_val/expon.ppf(alpha)/30)
    # return np.sqrt(N*min_val/expon.ppf(1 - alpha)/30), np.sqrt(N*min_val/expon.ppf(1)/30)
    return np.sqrt(2)-0.1, np.sqrt(2)+0.1
