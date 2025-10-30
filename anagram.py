def is_anagram(s1,s2):
    dict ={}


    for ch in s1:
        if ch not in dict:
            dict[ch]=1
        else:
            dict[ch]+=1
    
    for ch in s2:
        if ch not in dict:
            return False
        dict[ch]-=1
        if dict[ch]<0:
            return False
    return True

p = is_anagram('appwle','appleww')
print(p)

