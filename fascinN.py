def fascin(n):
    s=str(n*1)+str(n*2)+str(n*3)
    for n in check:
        if n not in s:
            return 'not fascinating'
    else:
        return 'fascinating'
n=192
check='123456789'
print(fascin(n))