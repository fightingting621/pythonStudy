for n in range (2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,'equals',x,'*',n//x)
            break#结束循环
        print(n, 'is a prime number')



for num in range(2,10):
    if num%2==0:
        print("Found an even number",num)
        continue#结束本次循环，回到外层循环
    print("Found a number",num)