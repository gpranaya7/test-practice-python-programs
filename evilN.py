def evil(n,count=0):
    while n!=0:
        rem=n%2
        if rem==1:
            count+=1
        n//=2
    if count%2==0:
        return 'evil'
    else:
        return 'odd'
n=23
power=1
print(evil(n))