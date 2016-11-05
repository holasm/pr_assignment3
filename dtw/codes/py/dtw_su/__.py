import mfcc
import dtw
import numpy as np
from numpy.linalg import norm

s1 = "../../../data/processed/test/Coimbatore.mfcc/1056_Coimbatore_.mfcc"
s2 = "../../../data/processed/train/Ariyalur.mfcc/1044Ariyalur_2.mfcc"

arr1 = np.array(mfcc.load_file(s1))
arr2 = np.array(mfcc.load_file(s2))

# a1 = arr1.reshape(400, 38)
# a2 = arr2.reshape(400, 38)

# f1 = open("test_1.txt", "w+")
# f2 = open("test_2.txt", "w+")

# for d1 in a1:
#   for d2 in d1:
#     f1.write(str(d2) + " ")
#   f1.write("\n")

dist = dtw.from_file(arr1, s2)
print dist
print norm(arr1)
print norm(arr2)
