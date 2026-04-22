sentence = input()
words = sentence.split()
print(words)
freq = {}
largest = 0

for word in words:
    freq[word] = len(word)
    if largest<len(word):
        largest = len(word)

for word,num in freq.items():
    if num == largest:
        print(f"{word} = {num}")