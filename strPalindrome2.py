def pali(s,res):
    res=s[::-1]
    if res==s:
        return 'palindrome'
    else:
        return 'not palindrome'
print(pali('abba',''))