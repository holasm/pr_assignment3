#DTW
############################
=> DTW for City names recognition from speech (https://github.com/holasm/pr_assignment3/tree/master/dtw)
############################

##Completed
----------------------------
1. Arrange all the .mfcc files to diffenent directory depending on city names  
2. Delete all folders having less than 20 {.mfcc} files
3. Separate 30% .mfcc files for each city 
4. Take one .mfcc file from test .mfcc files and calculate dtw distance from all remaining 70% data.
  The file giving least dtw distance from test .mfcc file will give the classification of the test city {test .mfcc used}
5. Repeat the step 4 for all test cities {.mfcc files for test cities}


##Status
----------------------------
###Stuck at

##Issues
---------------------------
1. All the code has been done in python so the processing is very very slow.
2. Will try to implement the dtw function using c++

##Todo
----------------------------
6. Process the test result and create the plots and report

#Resolved issues
-----------------------------
