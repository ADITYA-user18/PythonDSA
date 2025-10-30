s = "abcabcbb"

seen=set()
max_c=0


for i in range(0,len(s)):
    c_len=0
    for j in range(i,len(s)):
        if s[j] in seen:
            break
        seen.add(s[j])
        c_len+=1
        max_c=max(max_c,c_len)
print(max_c)




