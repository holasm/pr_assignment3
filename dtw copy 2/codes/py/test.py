from dtw_su import mfcc, dtw
import numpy as np


arr = mfcc.load_file('../../data/processed/Virudhunagar.mfcc/1222Virudhunagar_2.mfcc')
a = np.array(arr)
print(a)
# dtw.from_file('../../data/processed/Virudhunagar.mfcc/1222Virudhunagar_2.mfcc', arr)
