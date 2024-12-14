def fact(n,res=1):
    for fa in range(n,0,-1):
        res*=fa
    return res

print(fact(4))