for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,'equals',x,'*',n//x)
            break
    else:
            print(n,'is a prime number')    
for num in range(2,10):
     if num%2 ==0:
          print("Found an even number",num)
          continue
     print("Found a number", num)

def fib(n):
     a,b=0,1
     while a <n:
          print(a,end=' ')
          a,b=b,a+b
     print()
fib(2000)

f= fib
f(100)
fib(0)
print(fib(0))

def fib2(n):
     result=[]
     a,b=0,1
     while a<n:
          result.append(a)
          a,b =b,a+b
     return result
f100=fib2(100)
print("result: ",f100)