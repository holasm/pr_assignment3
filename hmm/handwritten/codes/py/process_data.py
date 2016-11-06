import mfcc
import os

rootDir = "./../../data/given/FeaturesHW/"
saveTo = "./../../data/processed/all/"

for dirName, subdirList, fileList in os.walk(rootDir):
  # print('Found directory: %s' % dirName)
  # cDirName = os.path.basename(os.path.normpath(dirName))
  for file in fileList:
    fname = file[:-4]
    path = rootDir + file
    mfcc.from_file_to_mfcc(path, saveTo, fname)
