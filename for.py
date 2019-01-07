#1.简单完成一个遍历输出功能
words=["a","beautiful","girl"]
for w in words:
    print(w,len(w))

#2.在数组位置插入内容
z=["My","name","is","fengtingting"]
for a in z[:]:
    if len(a)>3:
        words.insert(1,a)#在数组相应位置插入内容
print(words)

#3.迭代数字，内置函数range()
for i in range(20):#从0开始，输出到20，但不包括20
    print(i,end=",")
for a in range(5,10):#从5开始输出，一直到10，但不包括10
    print(a,end=" ")
for b in range(0,12,3):#从0到12，但是不包括12，输出3的倍数
    print(b)
for c in range(-10,-100,-30):#从-10到-100，加-30
    print(c)

oo=["I","have","a","good","friend"]
for i in range(len(oo)):
    print(i,oo[i])
print(range(5))#输出的是一个对象，是一个范围
print(list(range(5)))#输出的为一个数组，里面有每一个元素






