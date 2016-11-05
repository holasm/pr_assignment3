#!/usr/bin/env python
import os
import commands

def dozip(fromDir, toFile):
  cmd = 'tar -zcvf ' + toFile + ' ' + fromDir
  # print cmd
  res = commands.getstatusoutput(cmd)
  print res

def extract(fromFile, toPath='/'):
  cmd = 'gunzip < ' + fromFile + ' | tar -xv'
  # print cmd
  res = commands.getstatusoutput(cmd)
  print res
  