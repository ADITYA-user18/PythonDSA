nums = [1,2,1,4,4,4,5,5,5,5,6,7,7,8,8,8,8,8,8,1,1,1,1,1,1]

dict = {}


for num in nums:
     if num in dict:
          dict[num] +=1
     else:
          dict[num] =1
          
first_freq = 0
second_freq =0
first_key = None
second_key = None

for key in dict:
     value = dict[key]

     

     if value > first_freq:
          second_freq = first_freq
          second_key = first_key
          first_freq = value
          first_key = key
    
     
     elif value > second_freq:
          second_freq = value
          second_key = key


print(first_key,second_key)
