x=int(input("Please enter an integer:"))
if x<0:
    x=0
    print('Negative changed to zero',x)
elif x==0:#在选择判断中，条件后面以：结尾，elseif缩写成elif,保证格式
    print("Zero")
elif x==1:
    print("Single")
else:
    print(x)

y=int(input("Please input another integer:"))
if y>0:
    print("This is a Positive")
elif y<0:
    print("This is a Negative")
else:
    print(y)