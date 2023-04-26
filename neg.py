import numpy as np

def neg(s):

    if isinstance(s, float):
        return s

    if str(s) == 'nan':
        return np.nan

    s = s.replace(",", "")
    if s[0] == '(':
        return -float(s[1:-1])
    else:
        return float(s)

