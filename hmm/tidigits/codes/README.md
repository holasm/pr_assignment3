#HMM (HTK)
############################
=> TIDIGITS Dataset (https://github.com/holasm/pr_assignment3/tree/master/hmm_tigits)
############################

##Completed
----------------------------
1. Create {grammer} file  
-> HParse ...  
2. create {wlist} file  
3. create {lexicon} file  
-> HDMan ...  
4. create {man.mlf, woman.mlf} file  
5. create {man.scp, woman.scp} file  
6. merge the .mlf files
7. create {train.scp} file  √  
8. create {proto} file  √  
-> HCompV ...  
9. create {hmmdefs} file
10. no need to create {macros} file. we can use {vFloors} file
11. create the mlf
-> HERest ... (repeat 3 or more times)  
-> HVite ...  
-> HResults ...  

##Status
----------------------------
###Stuck at



##Todo
----------------------------


##Notes
-----------------------------
1. No need to create config file for HERest ... command.  

Regarding `$ HERest ...`  
1. We need to create mlf file with following format  
  
\#!MLF!#  
"*/14a.lab"  
one  
four  
.  
"*/15z2za.lab"  
one  
five  
two  
.  
"*/16a.lab"  
one  
six  
...  
   
***here "*/14a.lab" does not indicate any file, it indicates that the file 14a.htk is containg   
information about one and four in a sequence. Here 14a.htk is created using a matlab script or   
other means from mfcc files, created from speech audio. .mfcc files contains the features   
extracted from audio files.

NOTE: Do not give the path of .htk/.mfcc/.mfc or any other file.

#Resolved issues
-----------------------------
###1 . no need to use HCopy
-> HCopy -T 1 -C io/created/config -S io/created/scp/man.scp

ERROR [+6313]  OpenParmChannel: cannot read HTK Header in File /Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/hmm_tigits/data/tidigit/train/man/ae/12a.mfcc
  ERROR [+6313]  OpenAsChannel: OpenParmChannel failed
  ERROR [+6316]  OpenBuffer: OpenAsChannel failed
  ERROR [+1050]  OpenParmFile: Config parameters invalid
 FATAL ERROR - Terminating program HCopy

###2 .
-> HCompV 
No need to do HCompV ..

###3 .
-> HHEd ...  
No need to do HHEd ..

###4 .
