import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv("Ads_CTR_Optimisation.csv")

# Random Selection

"""
import random
N = 10000
d = 10
toplam = 0
secilenler = []
for n in range(0,N):
    ad = random.randrange(d)
    secilenler.append(ad)
    odul = data.values[n,ad]
    toplam = toplam + odul

plt.hist(secilenler)
plt.show()
"""

# UCB

N = 10000 # 10000 reklam gösterimi
d = 10 # toplam 10 ilan var
# Ri(n)
oduller = [0] * d # ilk başta bütün ilanların ödülü sıfır
# Ni(n)
tiklamalar = [0]*d # o ana kadarki tıklamalar
toplam = 0 # toplam ödül
secilenler = []
for n in range(0,N):
    ad = 0 # seçilen ilan
    max_ucb = 0 
    for i in range(0,d):
        ortalama = oduller[i] / tiklamalar[i]
        delta = math.sqrt(3/2*math.log(n)/tiklamalar[i])
        ucb = ortalama + delta
        if max_ucb < ucb: # max'tan büyük bir ucb çıktı
            max_ucb = ucb
            ad = i
    secilenler.append(ad)
    odul = data.values(n,ad)
    toplam = toplam + odul