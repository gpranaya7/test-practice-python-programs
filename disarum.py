def disarum(n,power,dup,res=0):
    while n!=0:
        rem = n%10
        res+=rem**power
        power-=1
        n//=10
    return dup==res
n=136
power=len(str(n))
print('disarum' if disarum(n,power,n) else 'not disarum')