student1=input("Enter the student name:")
s1_subject1=int(input("Enter student1 mark:"))
s1_subject2=int(input("Enter student1 mark:"))
s1_subject3=int(input("Enter stident1 mark:"))
total_s1=s1_subject1+ s1_subject2+s1_subject3
avg1=total_s1/3
print("total = ",total_s1)
print("avg = ",avg1)
student2=input("Enter the student name:")
s2_subject1=int(input("Enter student2 mark:"))
s2_subject2=int(input("Enter student2 mark:"))
s2_subject3=int(input("Enter stident2 mark:"))
total_s2=s2_subject1+ s2_subject2+s2_subject3
avg2=total_s2/3
print("total = ",total_s2)
print("avg = ",avg2)
student3=input("Enter the student name:")
s3_subject1=int(input("Enter student2 mark:"))
s3_subject2=int(input("Enter student2 mark:"))
s3_subject3=int(input("Enter stident2 mark:"))
total_s3=s3_subject1+ s3_subject2+s3_subject3
avg3=total_s3/3
print("total = ",total_s3)
print("avg = ",avg3)
if total_s1 > total_s2 and total_s1 > total_s3:
    print(student1,"got the greater mark")
elif total_s2 > total_s3 and total_s2 > total_s1:
    print(student2,"got the greater mark")
else:
    print(student3,"got the greater mark")
    
