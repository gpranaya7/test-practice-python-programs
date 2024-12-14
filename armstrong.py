def arm(n,power,dup,res=0):
    while n!=0:
        rem=n%10
        res+=rem**power
        n//=10
    return dup==res
n=152
power=len(str(n))
print('armstrong' if arm(n,power,n) else 'not armstrong')