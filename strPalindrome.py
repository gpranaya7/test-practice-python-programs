def pali(s):
    for ind in range(len(s)//2):
        if s[ind]!=s[-ind-1]:
            return 'not palidrome'
    else:
        return 'palindrome'

print(pali('abbna'))