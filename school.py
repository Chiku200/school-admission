import csv

def write_into_csv(info_list):
    with open('student_info.csv','a', newline= '') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact Number","Email"])

        writer.writerow(info_list)
if __name__== '__main__':
 condition = True

 while(condition):
   student_info = input("Enter student information in the following format (Name Age ontact_Number Email) :")
   print("Entered information:"+student_info)

   student_info_list = student_info.split('  ')
   print("Enter split up information is :"+str(student_info_list))
   
   
   write_into_csv(student_info_list)

   condition_check =input("Enter (yes/no)if you want to enter information")
   if condition_check == "yes":
         condition = True
   elif condition_check == "no":
             condition =False
