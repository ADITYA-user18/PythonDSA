num = 153

original = num

leng = len(str(num))

sums = 0

while(num>0):
    last_dight = num % 10
    sums += last_dight ** leng
    num = num//10


if(original == sums):
    print('Armstrong')
else:
    print(' Not ArmStrong')



'''

If the output will be same as the num value then it is called as the Armstrong Number

'''

