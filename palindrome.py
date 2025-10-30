# def palindrome(s):
#     l = len(s)
#     left = 0
#     right=l-1

#     while(left<right):
#         if s[left] != s[right]:
#             return False
#         left +=1
#         right -= 1
#         return True
    
# print(palindrome('nitin'))



'''

output :
True



For to check the sring is palindrome or not 


'''



## same using the recursion

def func(s,left,right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return func(s,left+1,right-1)
    
    



    
print(func('nitin',0,4))
        








