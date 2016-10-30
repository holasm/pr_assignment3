import mfcc
import numpy as np
import dtw_web
from numpy.linalg import norm

def my_custom_norm(x, y):
  return (x * x) + (y * y)

def cal_dtw(arr_1, arr_2):
  dist, cost = dtw_web.dtw(arr_1, arr_2, dist=my_custom_norm)
  return dist

def from_file(arr_2, filePath):
  arr_1 = np.array(mfcc.load_file(filePath))
  arr_2 = np.array(arr_2) # convert arr to numpy array
  # dist = cal_dtw(arr_1, arr_2)
  # print dist
  if(len(arr_1) == len(arr_2)):
    return norm(arr_1 - arr_2)
  else:
    return 1000
  # find dtw from arr
  # dtw_distance
  ### return dtw_distance

def from_mem(cityName_mfcc, testFileData):
  arr_1 = np.array(cityName_mfcc)
  arr_2 = np.array(testFileData)
  # print(arr_1)
  # print(arr_2)
  return 1
  # find dtw from arr
  # dtw_distance
  ### return dtw_distance