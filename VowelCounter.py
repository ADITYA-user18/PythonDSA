s="Aditya"
vowels = 'aeiouAEIOU'
TotalConsonents=0
TotalVowels = 0
for ch in s:
    if ch in vowels:
        TotalVowels+=1

    if ch not in vowels:
        TotalConsonents+=1

print("Vowels:",TotalVowels)
print("Consonents",TotalConsonents)