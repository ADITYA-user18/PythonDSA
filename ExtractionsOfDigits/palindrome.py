n = 121

original = n

reverse = 0

while(n>0):
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n//10

if(reverse == original):
    print('Palindrome')
else:
    print('Not a Palindrome')


# Alternative method not for interview 


# if str(n) == str(n)[::-1]:
#     print('yes')
# else:
#     print('no')



# TC - O(log10(n))
#SC - O(1)