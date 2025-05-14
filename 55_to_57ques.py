# 55 WAP to store name of subjects and their teachers in a dictionary

subject_teacher = { }

n = int(input("Enter number of subjects: "))
for i in range(n):
    subject = input(f"Enter subject {i+1} name:- ")
    teacher = input("Enter the subject Teacher name:- ")
    subject_teacher[subject] = teacher

print("Subject and Teacher Dictionary:- ", subject_teacher)

# 56 Search the teacher name corresponding to subject name and display it
subject = input("Enter the subject name to search teacher:- ")
if subject in subject_teacher:
    print(f"Teacher for {subject} is {subject_teacher[subject]}")
else:
    print("Subject not found in the dictionary")

#57 Update the teacher name corresponding to subject name if required
search_subject = input("Enter the subject name to update teacher:- ")
if search_subject in subject_teacher:
    teacher = input("Enter the new teacher name:- ")
    subject_teacher[search_subject] = teacher
    print(f"Updated teacher for {search_subject} is {subject_teacher[search_subject]}")