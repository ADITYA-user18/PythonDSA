n=123453254548656

sumOfDigits = 0

while(n>0):
    last_digit = n % 10
    sumOfDigits += last_digit
    n = n//10


print(sumOfDigits)