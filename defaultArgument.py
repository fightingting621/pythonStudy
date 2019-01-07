#1.默认参数
def ask_ok(prompt,retries=4,reminder='Please try again'):
    while True:
        ok=input(prompt)#prompt提示
        if ok in ("y","ye","yes"):
            return True
        if ok in ("n","no","non","none"):
            return False
        retries=retries-1#retries 重试
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok("Do you love me?")
ask_ok("OK,Let's go!",2)
ask_ok("Do you want play with me?",2,"Yes,I'd like~")
#2.
i=5
def f(arg=i):
    print(arg)
i=6
f()
#3.
def f(a,L=[]):
    L.append(a)
    return L
print(f(1,[22,3,4]))
print(f(2))#函数会累积在后续调用给他传递的参数
print(f(3))


