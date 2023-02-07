# 判断是不是素数
def number(a):
    for i in range(2, a):
        if a % i == 0:

            print("False")
            break
        if i == a-1:
            print("True")


number(7)

# 判断最大公约数和最小公倍数


def fun(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            print(i)


def fun2(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            print(x*y//i)


fun(13, 26)
fun2(25, 45)
