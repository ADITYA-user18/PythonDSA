def f(sum,i,n):
    if i>n:
        print(sum)
        return
    f(sum+i,i+1,n)
f(0,1,4)



'''
here sum of n numbers is calculated using the recursion method
'''