def tech(n):
    res=(int(s[:half])+int(s[half:]))**2
    if res==n:
        return 'tech'
    else:
        return 'not'


n=2025
s=str(n)
half=len(str(n))//2
print(tech(n))
