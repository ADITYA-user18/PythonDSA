nums = [10, 5, 8, 20, 2]

first = float('-inf')
second = float('-inf')

for num in nums:
    if num>first:
        second = first
        first = num
    else:
        if num > second and num != first:
            second = num

if(second == float('-inf')):
    print('No Second Largest')
else:
    print(second)
   