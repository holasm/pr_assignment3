import numpy as np
from math import floor


def first_derivative(arr, t, startIndex):
  div = 5
  if( t>=2 and t<=len(arr)-2 ):
    x1 = ( (1*(arr[t+1, startIndex+0])- arr[t-1, startIndex+0])) + (2*(arr[t+2, startIndex+0]- arr[t-2, startIndex+0]) ) / (div)
    y1 = ( (1*(arr[t+1, startIndex+1])- arr[t-1, startIndex+1])) + (2*(arr[t+2, startIndex+1]- arr[t-2, startIndex+1]) ) / (div)
    return round(x1,5), round(y1,5)

def curvature(arr, t):
  div = (arr[t][2]**2 + arr[t][3]**2)**1.5
  if div == 0:
    c = ((arr[t][2] * arr[t][5]) - (arr[t][4] * arr[t][5])) / 0.00001
  else:
    c = ((arr[t][2] * arr[t][5]) - (arr[t][4] * arr[t][5])) / div
  return [round(c,5)]

def extend(str):
  arr_1 = []
  arr_2 = []
  arr_ = []

  data = str.strip().split(' ')

  # convert to float array
  for i in range(1, len(data)):
    arr_.append(float(data[i]))
    
  # reshape to 2 column matrix
  arr = np.reshape(arr_, (-1, 2))

  # arr = arr.tolist()
  for i in range(2, len(arr)-2):
    pair = first_derivative(arr, i, 0)
    arr_1.append(np.concatenate((arr[i], pair), 0).tolist())
  # arr = arr[2:-2] # trim first and last two pair
    
  arr_1 = np.array(arr_1)
  for i in range(2, len(arr_1)-2):
    pair = first_derivative(arr_1, i, 2)
    arr_2.append(np.concatenate((arr_1[i], pair), 0).tolist())

  # calculate curvature
  for i in range(0, len(arr_2)):
    arr_2[i] = arr_2[i] + curvature(arr_2, i)

  return arr_2

# print extend("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18")









