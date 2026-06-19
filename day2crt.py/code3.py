#STRINGS METHODS,PALINDROME,ANAGRAM PROBLEMS

#https://markdownviewer.org/#topic-4-list-operations
s = "aaabbbcccc"
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count =count+ 1
    else:
        print(s[i-1] + str(count), end="")
        count = 1

print(s[-1] + str(count))