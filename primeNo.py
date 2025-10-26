def PrimeNo(num):
    if num == 1 :
        return 1
    for i in range(2,num):
        if num % i == 0:
            print('Not a Prime')
            break
    else:
        print('prime')
    return ''

a=PrimeNo(2)
print(a)
