import os
import operator
import random
from dtw_su import mfcc, dtw
import numpy as np
import datetime
import threading
import commands

# def do_file(testFilePath):
#   # Set the directory you want to start from
#   fos = open('test.txt', 'w')
#   database = {}
#   rootDir = '../../data/processed'
  
#   # *****************************
#   # LOAD TEST FILE DATA
#   # *****************************
#   testFileData = mfcc.load_file(testFilePath)

#   # ****************************************************
#   # calculate dtw distance for all files and take the average
#   # ****************************************************
#   for dirName, subdirList, fileList in os.walk(rootDir):
#     # print('Found directory: %s' % dirName)
#     cDirName = os.path.basename(os.path.normpath(dirName))
#     database[cDirName] = []
#     for fname in fileList:
#       # basePath = cpath[:(-len(__file__)-1)]
#       basePath = os.path.join(rootDir, cDirName)
#       basePath = os.path.join(basePath, fname)
      
#       # print basePath
#       # fos.write(basePath + '\n')
#       # print(dirName)

#       # 
#       # READ THE FILE AND CALCULATE THE DTW DISTANCE
#       # SAVE THE DTW DISTANCE
#       #
#       # call dtw.from_file
#       print 'Calc dtw from' + testFilePath + '=>' + fname
#       dtw_distance = dtw.from_file(testFileData, basePath)
#       print 'Calculated distance is: ->' + str(dtw_distance)
#       (database[cDirName]).append(dtw_distance)

#     # take average of the total dtw distace from all cities
#     database[cDirName] = np.mean(np.array(database[cDirName]))

#   maxVal = min(database.iteritems(), key=operator.itemgetter(1))[0]
#   fos.write(str(database))
#   return {testFilePath:maxVal}
# # end_do_file

def singleCityClassify(testCityFilePath, mem, testResult={}):
  count = 1;
  database = {}
  cityName_mfcc_ = os.path.basename(os.path.normpath(testCityFilePath))
  cityName_ = testCityFilePath[1:-len(cityName_mfcc_)-1]
  cityName_ = os.path.basename(os.path.normpath(cityName_))
  # if file alrady exists inside su/result then skip
  # *****************************
  # LOAD TEST FILE DATA
  # *****************************
  testFileData = mfcc.load_file(testCityFilePath)
  # count = 1
  
  testFileName = testCityFilePath[-len(cityName_mfcc_):]
  print testFileName
  sf = open('./../../su/log/' + testFileName +'.log', 'a+')

  for dirName in mem:
    cityName_mfcc = os.path.basename(os.path.normpath(dirName))
    cityName = dirName[1:-len(cityName_mfcc)-1]
    cityName = os.path.basename(os.path.normpath(cityName))

    if not cityName in database: # if empty
      # print(str(count) + ' -> ' +cityName + ' not in database')
      # count = count+1
      database[cityName] = []

    # ---------------------------------------------------------
    # calculate dtw.from_mem b/w testFileData and mem
    print count
    count = count + 1
    sf.write(str(count) + '\n')
    print 'Calc dtw from' + testCityFilePath + '=>' + dirName
    sf.write('Calc dtw from' + testCityFilePath + '=>' + dirName + '\n')
    # ---------------------------------------------------------

    # print threading.currentThread().ident
    dtw_distance = dtw.from_mem(testFileData, mem[dirName])
    
    # ---------------------------------------------------------
    print 'Calculated distance is ->' + str(dtw_distance)
    sf.write('Calculated distance is ->' + str(dtw_distance) + '\n')
    # ---------------------------------------------------------

    (database[cityName]).append(dtw_distance)
    
  sf.close()
  for city in database:
    # take average of the total dtw distace from all cities
    database[city] = np.mean(np.array(database[city]))

  minCity = min(database.iteritems(), key=operator.itemgetter(1))[0]
  minVal = min(database.iteritems(), key=operator.itemgetter(1))[1]


  # return minVal or 
  item = {
    testCityFilePath: minCity,
    'val': minVal
  }
  if not cityName_ in testResult: # if empty
    testResult[cityName_] = []

  print 'Done ' + cityName_mfcc_
  testResult[cityName_].append(item)

# end_singleCityClassify

def do_mem(testCityFilePaths):
  # Set the directory you want to start from
  # fos = open('test.txt', 'wa')
  rootDir = '../../data/processed/'
  cmd = 'rm ' + rootDir + '.DS_Store'
  # print cmd
  # res = commands.getstatusoutput(cmd)

  mem = {}
  testResult = {}

  # ****************************************************
  # calculate dtw distance for all files and take the average
  # ****************************************************
  for dirName, subdirList, fileList in os.walk(rootDir):
    # print('Found directory: %s' % dirName)
    cDirName = os.path.basename(os.path.normpath(dirName))
    for fname in fileList:
      filePath = os.path.join(rootDir, cDirName)
      filePath = os.path.join(filePath, fname)

      # 
      # READ THE FILES AND SAVE ON mem DICTIONARY
      #
      # mem[filePath] = mfcc.load_file(filePath)
      # mfcc.load_file_to(filePath, mem)
      t = threading.Thread(target=mfcc.load_file_to, args=(filePath, mem))
      t.start()
      t.join()

  # *************************************************
  # NOW REUSE mem TO DO CLASSIFICATION MULTIPLE TIMES
  # *************************************************
  for testCityFilePath in testCityFilePaths:
    # 
    # USE threading here for multiple classification parallesism
    # 
    # singleCityClassify(testCityFilePath, mem, testResult)
    t = threading.Thread(target=singleCityClassify, args=(testCityFilePath, mem, testResult))
    t.start()
    t.join()
    print datetime.datetime.now()
  
  for cityName_ in testResult:
    sf = open('./../../su/result/' + cityName_, 'a+')
    sf.write(str(testResult[cityName_]))
    sf.close()
  # end for testFiles
  return testResult
