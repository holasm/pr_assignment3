import classify
import datetime
from dtw_su import classify

testFiles = [
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Ariyalur.mfcc/1041Ariyalur_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Ariyalur.mfcc/1044Ariyalur_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore.mfcc/1054Coimbatore_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore.mfcc/1059_Coimbatore_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore.mfcc/1059_Coimbatore_3.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore.mfcc/1059_Coimbatore_4.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore.mfcc/1060Coimbatore_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore.mfcc/1061Coimbatore_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore.mfcc/1062Coimbatore_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore.mfcc/1062_Coimbatore_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore.mfcc/1070_Coimbatore_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore.mfcc/1075_Coimbatore_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore.mfcc/1077Coimbatore_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore.mfcc/1081Coimbatore_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore_maavat$t$am.mfcc/1084_Coimbatore_maavat$t$am_4.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore_maavat$t$am.mfcc/1084_Coimbatore_maavat$t$am_5.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore_maavat$t$am.mfcc/1086Coimbatore_maavat$t$am_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore_maavat$t$am.mfcc/1086_Coimbatore_maavat$t$am_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore_maavat$t$am.mfcc/1086_Coimbatore_maavat$t$am_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore_maavat$t$am.mfcc/1086_Coimbatore_maavat$t$am_3.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Coimbatore_maavat$t$am.mfcc/1086_Coimbatore_maavat$t$am_4.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Cuddalore.mfcc/1263_Cuddalore_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Cuddalore.mfcc/1269Cuddalore_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Cuddalore.mfcc/1269_Cuddalore_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Dindigul.mfcc/1174Dindigul_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Dindigul.mfcc/1186_Dindigul_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Dindigul.mfcc/1198Dindigul_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Dindigul.mfcc/1200Dindigul_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Dindigul.mfcc/1201_Dindigul_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode.mfcc/1067_Erode_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode.mfcc/1067_Erode_3.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode.mfcc/1068Erode_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode.mfcc/1069Erode_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode.mfcc/1069_Erode_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode.mfcc/1069_Erode_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode.mfcc/1069_Erode_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode.mfcc/1069_Erode_3.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode.mfcc/1070_Erode_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode_maavat$t$am.mfcc/1071_Erode_maavat$t$am_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode_maavat$t$am.mfcc/1071_Erode_maavat$t$am_3.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode_maavat$t$am.mfcc/1071_Erode_maavat$t$am_4.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode_maavat$t$am.mfcc/1072Erode_maavat$t$am.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Erode_maavat$t$am.mfcc/1072_Erode_maavat$t$am_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Karur.mfcc/1184Karur_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Karur.mfcc/1184_Karur_.mfcc"
]
city = classify.do_mem(testFiles, './../../su/result/')

print(city)



# find_max(database)





