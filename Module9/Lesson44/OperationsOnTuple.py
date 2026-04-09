# Write a program to create a tuple and perform the mentioned operations on that tuple

My_Tuple = ()
print(My_Tuple)

My_Tuple2 = (1,2,3)
My_Tuple3 = (1, "Hi", 3.1)
print(My_Tuple3)

My_Tuple4 = ("Hello", [1,2,3], (2,3,4)) # This is a Nested Tuple
print(My_Tuple4[2][1])
print(My_Tuple4[1])

My_Tuple5 = ('h','e','l','l','o')
print(My_Tuple5[3])
print(My_Tuple5[1:3])

for i in My_Tuple5:
    print("Hello", i)