n = 153

original = n
summer =0
length = len(str(n))

while n>0:
    last_digit = n % 10
    summer+= last_digit ** length
    n = n // 10

if original == summer:
    print('yes')
else:
    print('not')