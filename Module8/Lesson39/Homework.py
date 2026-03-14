
total_days = int(input("Enter total number of working days: "))
absent_days = int(input("Enter total number of days absent: "))

attended_days = total_days - absent_days

percentage = (attended_days / total_days) * 100
print("Attendance Percentage:", percentage)

if percentage < 75:
    print("Student is not allowed to sit in the exam.")
else:
    print("Student is allowed to sit in the exam.")