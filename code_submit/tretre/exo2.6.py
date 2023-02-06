#exo 找素数 can only be divised by 1 and itself
def primnb():
    n = int(input())
    for i in range(2,n):
        if n%i == 0:
            return False
            break
        else:
            return True
primnb()

#最大公约数和最小公倍数
def fun(nb1,nb2):
    if nb1 < nb2:
        min = nb1
    else:
        min = nb2
    for i in range(1,min+1):
        if (nb1%i==0) and (nb2%i==0):
            gys = i
            gbs = nb1*nb2/gys
return gys,gbs
