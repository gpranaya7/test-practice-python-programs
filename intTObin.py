def bin(n,res=0,power=1):
    while n!=0:
        rem=n%2
        res+=power*rem
        n//=2
        power*=10
    return res
n=2
print(bin(n))
