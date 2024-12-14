def pali(num,dup,res=0):
    while num!=0:
        rem=num%10
        res=res*10+rem
        num//=10
    return res==dup
num=123
print('palidrome' if pali(num,num) else 'not palindrome')