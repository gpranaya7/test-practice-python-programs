
def fact(n,mul=1):
    for fa in range(n,0,-1):
        mul*=fa
    return mul


def strong(n,dup,res=0):
    while n!=0:
        rem=n%10
        res+=fact(rem)
        n//=10
    return dup==res
n=146
print('strong' if strong(n,n) else 'not')
    