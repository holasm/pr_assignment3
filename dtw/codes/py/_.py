import classify
import datetime
from dtw_su import classify

testFiles = [
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Appil.mfcc/1022_Appil.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Salem.mfcc/1021Salem.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Thanjavur.mfcc/1021Thanjavur.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Theni.mfcc/1021Theni.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Villupuram.mfcc/1021Villupuram.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Ariyalur.mfcc/1022Ariyalur.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Chennai.mfcc/1022Chennai.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Coimbatore.mfcc/1022Coimbatore.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Madurai.mfcc/1022Madurai.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Nagapattinam.mfcc/1022Nagapattinam.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Theni.mfcc/1022Theni.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Thiruchirappalli.mfcc/1022Thiruchirappalli.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Thirunelveli.mfcc/1022Thirunelveli.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Thiruvannamalai.mfcc/1022Thiruvannamalai.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Virudhunagar.mfcc/1022Virudhunagar.mfcc',
  '/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/Appil.mfcc/1022_Appil.mfcc'
]
city = classify.do_file(testFiles[0])

print(city)



# find_max(database)





