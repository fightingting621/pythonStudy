def fib(n):#定义函数关键字 函数名（参数）
    a,b=0,1
    while a<n:
        print(a,end=" ")
        a,b=b,a+b
    print()#不管有没有这句话该函数都会打印和执行
fib(2000)#调用函数
#

def fib2(n):
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)#在该数组末尾加入元素
        a,b=b,a+b
    return result
f100=fib2(100)
f100
