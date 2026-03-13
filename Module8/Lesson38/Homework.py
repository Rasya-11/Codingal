#Raj scored 40, 70, 50 and 60 out of 100 in maths, science, Hindi and English. 
# Find the percentage he got.

maths = 40
science = 70
hindi = 50
english = 60

total_marks = maths + science + hindi + english
print("Total Marks:", total_marks)

percentage = total_marks / 400 * 100
#print("Percentage:", round(percentage,2))
print(f"Percentage: {percentage:.2f}")