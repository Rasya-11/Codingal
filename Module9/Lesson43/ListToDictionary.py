# Write a program to create a List with five students' details (roll no, name, grade). 
# Then convert that list into a dictionary.

# Students = [[1,'Priya',8],[2,'Ben',9],[3,'Holly',8]]
# def test(Students):
#     result = {}
#     for a in Students:
#         result[a[0]] = a[1:] #a[0] First element is the id, example: 1. a[0]: everything after first element like name and class, e.g. ['Priya', 8]
#     return result
# print("The original list is", Students)
# print("The converted list to dictioanry is", test(Students))


Students = [[1,'Priya',8],[2,'Ben',9],[3,'Holly',8]]
def test(Students):
    result = {}
    for a in Students:
        result[a[1]] = [a[0],a[2]]
    return result
print("The original list is", Students)
print("The converted list to dictioanry is", test(Students))