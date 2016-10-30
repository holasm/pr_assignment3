HMM (HTK)
############################
=> TIDIGITS Dataset (https://github.com/holasm/pr_assignment3/tree/master/hmm_tigits)
############################

#Completed
----------------------------
1. Create {grammer} file  
-> HParse ...  
2. create {wlist} file  
3. create {lexicon} file  
-> HDMan ...  
4. create {man.mlf, woman.mlf} file  
5. create {man.scp, woman.scp} file  
-> HCopy ...  
6. create {train.scp} file  √  
7. create {proto} file  √  
-> HCompV ...  


#Status
----------------------------
##Stuck at



#Todo
----------------------------
-> HERest ... (repeat 3 or more times)  
-> HHEd ...  
-> HVite ...  
-> HResults ...  

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