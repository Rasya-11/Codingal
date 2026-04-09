# Write a Python program to count the number of strings where the string length is two or more, 
# and the first and last characters are the same from a given list of strings.


# if len(i)>1 and i[0]==i[-1]:

def count_strings(str_list):
    count = 0

    for i in str_list:
        if len(i) > 1 and i[0] == i[-1]:
            count += 1

    return count
words = ["abc", "aba", "1221", "xyx", "a", "bb", "xyz"]

print("Original list:", words)
print("Count of matching strings:", count_strings(words))