# Q15: All Character Frequencies Same
# Check if all characters have same frequency

# Input: Get string
str = input()

# Initialize frequency dictionary
freq = {}

# Count frequency of each character
for ch in str:
    freq[ch] = freq.get(ch,0)+1

# Check if all frequencies are same
# Convert frequency values to set - if length is 1, all are same
if (len(set(freq.values())))==1:
    print("true")
else:
    print("false")