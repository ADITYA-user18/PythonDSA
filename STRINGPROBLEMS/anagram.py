def is_anagram(s1,s2):
    dict1 = {}
    dict = {}

    for ch in s1:
        if ch not in dict1:
            dict1[ch] = 1
        else:
            dict1[ch]+=1


    for ch in s2:
        if ch not in dict:
            dict[ch] = 1
        else:
            dict[ch]+=1
    
    return dict == dict1
        
        

            
        

s1 = 'Apple'
s2 = 'ppAel'

b = is_anagram(s1,s2)
print(b)

   
