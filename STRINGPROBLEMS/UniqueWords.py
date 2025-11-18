s = "abcabcbb"


seen = set()


for ch in s:
    if ch not in seen:
        seen.add(ch)
        print(ch)