def special(n,res=0):
    for fa in range(1,n//2+1):
        if n%fa==0:
            res+=fa
    return res==n

n=7
print('special number' if special(n) else 'not ')