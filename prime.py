def prime(n):
    for fa in range(2,n//2+1):
        if n%fa==0:
            return 'not prime'
        else:
            return ' prime'
print(prime(22))