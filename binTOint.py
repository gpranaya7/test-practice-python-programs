def intBin(n,power=0,res=0):
    while n!=0:
        rem=n%10
        res+=rem*(2**power)
        n//=10
        power+=1
    return res
n=10
print(intBin(n))