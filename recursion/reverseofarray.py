# array = [1,5,8,62,3,1,6,5,6,8,7,6,4]
# start,end = 1,5
# new_array = array[:start] + array[start:end+1][::-1]+array[end+1:]
# print(new_array)



'''

output:

[1, 1, 3, 62, 8, 5, 6, 5, 6, 8, 7, 6, 4]

reversing the array of only the index from 1 to 5 are reversed
'''


# Using the for loop
# array = [1,5,8,62,3,1,6,5,6,8,7,6,4]

# start,end = 3,5
# new_array = []

# for i in range(len(array)):
#     if (i < start):
#         new_array.append(array[i])
#     elif(start<= i <=end):
#         new_array.append(array[end-(i-start)])
#     else:
#         new_array.append(array[i])
# print(new_array)


# only even indices


# array = [1,5,8,62,3,1,6,5,6,8,7,6,4]

# new_arr = []

# for i in range(len(array)):
#     if(i%2==0):
#         new_arr.append(array[i])

# for val in new_arr[::-1]:
#     print(val)      


#Reversing the Entire Array

# array = [1,5,8,62,3,1,6,5,6,8,7,6,4]

# for val in array[::-1]:
#     print(val,end=' ')




# using the recursion technique


array = [1,5,8,62,3,1,6,5,6,8,7,6,4]
def func(array,left,right):
    if left > right:
        return
    array[left],array[right] = array[right],array[left]
    func(array,left+1,right-1)

func(array,3,6)
print(array)

