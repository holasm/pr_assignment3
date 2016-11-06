import classify
import datetime
from dtw_su import classify

testFiles = [
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Karur.mfcc/1184_Karur_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Karur.mfcc/1186Karur_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Karur.mfcc/1187Karur_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Madurai.mfcc/1246Madurai_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Madurai.mfcc/1255Madurai_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Madurai.mfcc/1255Madurai_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Namakkal.mfcc/1140Namakkal_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Namakkal.mfcc/1141Namakkal_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Perambalur.mfcc/1312_Perambalur_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Perambalur.mfcc/1312_Perambalur_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Perambalur.mfcc/1312_Perambalur_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Perambalur.mfcc/1312_Perambalur_3.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Perambalur.mfcc/1312_Perambalur_5.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Perambalur.mfcc/1314_Perambalur_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Perambalur.mfcc/1314_Perambalur_4.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Perambalur.mfcc/1316_Perambalur_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Perambalur.mfcc/1316_Perambalur_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Perambalur.mfcc/1316_Perambalur_3.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Salem.mfcc/1109_Salem_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Salem.mfcc/1110Salem_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Salem.mfcc/1110_Salem_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Salem.mfcc/1112Salem_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Salem.mfcc/1113Salem_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Salem.mfcc/1115Salem_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thanjavur.mfcc/1198Thanjavur_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thanjavur.mfcc/1198_Thanjavur_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thanjavur.mfcc/1286Thanjavur_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thanjavur.mfcc/1293Thanjavur_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Theni.mfcc/1047Theni_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Theni.mfcc/1101Theni_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Theni.mfcc/1101_Theni_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruchirappalli.mfcc/1134Thiruchirappalli_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruchirappalli.mfcc/1134_Thiruchirappalli_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruchirappalli.mfcc/1135Thiruchirappalli_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruchirappalli.mfcc/1137Thiruchirappalli_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruchirappalli.mfcc/1137_Thiruchirappalli_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruchirappalli.mfcc/1137_Thiruchirappalli_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruchirappalli.mfcc/1138Thiruchirappalli_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruchirappalli.mfcc/1138_Thiruchirappalli_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thirunelveli.mfcc/1266_Thirunelveli_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thirunelveli.mfcc/1266_Thirunelveli_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thirunelveli.mfcc/1271Thirunelveli_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thirunelveli.mfcc/1271_Thirunelveli_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thirunelveli.mfcc/1272Thirunelveli_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thirunelveli.mfcc/1273_Thirunelveli_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thirunelveli.mfcc/1273_Thirunelveli_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruvannamalai.mfcc/1270Thiruvannamalai_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruvannamalai.mfcc/1270_Thiruvannamalai_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruvarur.mfcc/1302Thiruvarur_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruvarur.mfcc/1303Thiruvarur_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruvarur.mfcc/1309Thiruvarur_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruvarur.mfcc/1309_Thiruvarur_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Thiruvarur.mfcc/1310Thiruvarur_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Tirupur.mfcc/1200_Tirupur_3.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Tirupur.mfcc/1201_Tirupur_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Tirupur.mfcc/1201_Tirupur_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Tirupur.mfcc/1201_Tirupur_3.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Tirupur.mfcc/1201_Tirupur_4.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Villupuram.mfcc/1138Villupuram_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Villupuram.mfcc/1138_Villupuram_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Villupuram.mfcc/1187Villupuram_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Virudhunagar.mfcc/1174Virudhunagar_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Virudhunagar.mfcc/1175_Virudhunagar_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Virudhunagar.mfcc/1175_Virudhunagar_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Virudhunagar.mfcc/1178Virudhunagar_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Virudhunagar.mfcc/1178_Virudhunagar_.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Virudhunagar.mfcc/1179Virudhunagar_1.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Virudhunagar.mfcc/1179Virudhunagar_2.mfcc",
"/Users/subhasis/Documents/iitm_courses/1_st_sem/PR/pr_assignment/assignment_3/dtw/data/processed/test/Virudhunagar.mfcc/1180Virudhunagar_1.mfcc"
]
city = classify.do_mem(testFiles, './../../su/result_2/')

print(city)



# find_max(database)





