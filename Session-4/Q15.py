str = input()
freq = {}
for ch in str:
    freq[ch] = freq.get(ch,0)+1

if (len(set(freq.values())))==1:
    print("true")
else:
    print("false")