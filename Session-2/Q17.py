def palindrome(str):
    rev = str[::-1]
    if(rev==str):
        return "True"
    else:
        return "False"
text = input()
print(palindrome(text))

