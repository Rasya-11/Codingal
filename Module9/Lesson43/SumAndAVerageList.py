# Write a Python program to find the sum and average of the list. 
# The average of the list is defined as the sum of the elements divided by the number of the elements. 
# Also, find the largest and the smallest number in the list.

# List=[10,20,30,40,15]

# Use for loop, sum=sum+i

# avg=sum/len(List)

#Sort the list first and smallest number = 1st item (index 0), largest number = last item

List = [10, 20, 30, 40, 15]

total = 0
for i in List:
    total = total + i

avg = total / len(List)

List.sort()

smallest = List[0]
largest = List[-1]

print("List:", List)
print("Sum:", total)
print("Average:", avg)
print("Smallest number:", smallest)
print("Largest number:", largest)