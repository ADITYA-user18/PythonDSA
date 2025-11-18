num = 1221
original = num
rev= 0

while(num>0):
    last_digit = num % 10
    rev = rev * 10 + last_digit
    num = num // 10



if ( rev == original):
    print('Yes The no is Palindrome')
else:
    print('No the Number is not Palindrome')


    
    