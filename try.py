#1
'''
user_id = "gowri"
password = 8001
otp=1234

insta_id = input("Enter the Instagram user ID: ")

if insta_id == user_id:
    pas = int(input("Enter the password: "))
    if pas == password:
        print("Login successful")
    else:
        print("Invalid password")

    otp_user=int(input("enter the otp "))
    if otp_user==otp:
        print("otp verified")
    else:
        print("otp denied")
else:
    print("Login denied")
'''
from nt import remove

#2
'''
N = int(input("Enter the marks obtained: "))

if 90 <= N <= 100:
    print("Grade A")
elif 70 <= N <= 89:
    print("Grade B")
elif 50 <= N <= 69:
    print("Grade C")
elif 35 <= N <= 49:
    print("Grade D")
else:
    print("Fail")
'''
#3
'''
a=[1,2,3,4,'hi']
for i in range (0,5):
    if type(a[i]) in (int ,float,bool,complex):
        print("Single value datatype")
    else:
        print("multivalue datatype")
'''
#4
'''
i=1
print("even numbers betweeen 1-10")
while i<=10:
    if i%2==0:
        print(i)
    i+=1
print("odd numbers between 1-10")
i=1
while i<=10:
    if i%2==1:
        print(i)
    i+=2
'''
#5
'''
i=0
sum=0
print("sum of even numbers betweeen 1-10")
while i<=10:
    if i % 2 == 0:
        sum += i
    i+=1
print(sum)

i=0
sum=0
print("sum of odd numbers betweeen 1-10")
while i<=10:
    if i % 2 == 1:
        sum += i
    i+=1
print(sum)
'''
#6
'''
a=[1,2,3,4]
x=sum(a,7)
print(x)
'''
#7

'''a=[1,2,3,4,'hi']
i=0
while i<len(a):
    if type(a[i]) in (int ,float,bool,complex):
        print(a[i]," is Single value datatype")
    else:
        print(a[i]," is Multivalue datatype")
    i=i+1
'''
#8
'''
a="swapnodaya"
i=0
while i<len(a):
    if i%2==0:
        print(a[i])
    i=i+1
'''
#9
'''
a="2ew24cs040#"
i=0
print("Num=",end='')
while i < len(a):
    if '0'<=a[i]<='9':
        print(a[i],end='')
    i=i+1
print('')
print("Alp=",end='')
i=0
while i < len(a):
    if 'a'<=a[i]<='z':
        print(a[i],end='')
    i=i+1
print('')
print("Sp=",end='')
i=0
while i < len(a):
    if 'a'<=a[i]<='z' or '0'<=a[i]<='9':
        print('',end='')
    else:
        print(a[i],end='')
    i=i+1
'''
#10
'''
a="2ew24cs040#"
i=0
num=" "
alp=" "
sp=" "
while i < len(a):
    if '0'<=a[i]<='9':
        num+=a[i]
    elif 'a'<=a[i]<='z' or '0'<=a[i]<='9':
        alp+=a[i]
    else:
        sp+=a[i]
    i+=1
print(num)
print(alp)
print(sp)
'''
#11
'''
a="2ew24cs040#"
i=0
ncount=0
acount=0
scount=0
num=" "
alp=" "
sp=" "
while i < len(a):
    if '0'<=a[i]<='9':
        num+=a[i]
        ncount+=1
    elif 'a'<=a[i]<='z' or 'A'<=a[i]<='Z':
        alp+=a[i]
        acount+=1
    else:
        sp+=a[i]
        scount+=1
    i+=1
print(num,ncount)
print(alp,acount)
print(sp,scount)
'''
#12
'''
a="2ew&24cs040#@"
i=0
sp=" "
while i < len(a):
    if not ('0'<=a[i]<='9' or ('a'or'A')<=a[i]<=('z'or'Z')):
        sp+=a[i]
    i=i+1
print(sp)
'''
#13
'''
i=0
d=[]
c=['hi','90','hello',90,0.2, {3},0+0j]
while i<len(c):
    if type(c[i]) is (str) :
        d=d+[c[i]]
    i=i+1
print(d)
'''
#14
'''
i=0
e="hEllo"
f=0
while i<len(e):
    if e[i] in ("aeiouAEIOU"):
        f=f+1
    i=i+1
print(f)
'''
#15
'''
b=[0,1,12,20,3,12,5,28,25]
i=0
sum=0
c=[]
while i<len(b):
    if b[i]%2==1:
        sum=sum+b[i]
    i=i+1
c=c+[sum]
print(c)

'''

#16
'''
a=['Hi','hello','bye','Python','sql']
i=0
n=[]
while i<len(a):
    if a[i] in 'A'<=n<='Z':
        print(a[i])
    i+=1
print
'''

'''
y="Python"
z=""
i=len(y)-1
while i>=0:
    z+=y[i]
    i-=1
print(z)'''

'''
e=["Hi","Python"]
g=[]
count=0
i=0
j=0
while i<len(e):
    while j<len(e[i]):
        count+=1
        j+=1
    g=g+[count]
    i+=1
print(g)
'''
'''
D="Hi"
E=["Python","Sql"]
F={}
i=0
while i<len(D) and i<len(F):
    F[D[i]]=E[i]
    i+=1
print(F)
'''

'''
e=["Python","Sql"]
d=[]
f={}
i=0
while i<len(e):
    count = 0
    j = 0
    while j<len(e[i]):
        count+=1
        j+=1
    d=d+[count]
    f[e[i]]=d[i]
    i+=1
print(f)
'''
'''
P = "aabbccc"
V = ""
i = 0

while i < len(P):
    count = 1
    j = i + 1
    while j < len(P) and P[i] == P[j]:
        count += 1
        j += 1
    V += P[i] + str(count)
    i = j

print(V)
'''
'''
num = int(input("Enter a number: "))
if num < 2:
    print(f"{num} is not a prime number.")
else:
    d = 2
    prime = True
    while num>d:
        if num % d == 0:
            prime = False
        d += 1
    if prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
'''

'''
n=int(input("Enter a number:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)
'''

'''num = int(input("Enter a number: "))
i = 1
s = 0

while i < num:
    if num % i == 0:
        s += i
    i += 1

if s == num:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
'''
'''
d=["Python","Sql"]
e=[]
i=0
j=0
for i in d:
    c=0
    for j in i:
        c=c+1
    e=e+[c]
print(e)'''

'''
d = ['Hello', 'Hi']
e = []
i=0
j=0
for i in d:
    c = 0
    for j in i:
        if j in "aeiouAEIOU":
            c=c+1
    e=e+[c]
print(e)
'''

'''
d = ['Hello', 'Hi']
e = []
i=0
j=0
for i in d:
    c = 0
    for j in i:
        if j not in "aeiouAEIOU":
            c=c+1
    e=e+[c]
print(e)
'''

'''
d = ['Python','Workshop']
e = []
i=0
j=0
res=0
for i in d:
    c = 0
    for j in i:
        c=c+1
    res=c//2
    e=e+(res)
print(e)
'''
'''d = ['Python', 'Workshop']
e = []
i=0
j=0
for i in d:
    c = 0
    for j in range(len(i)):
        if j%2==0:
            c += 1
    e=e+[c]
print(e)
'''

'''z="abbacb"
d=" "
for i in z:
    count=0
    if i not in d:
        for j in z:
            if i==j:
                count+=1
        d+=i+str(count)
print(d)

z="abbacc"
d=""
e=""
for i in z:
    count=0
    if i not in d:
        for j in z:
            if i==j:
                count+=1
        e+=str(count)
        d+=i
print(d,end='')
print(e)
'''

'''def is_even(a):
    if a%2==0:
        print(a,"is even")
    else:
        print(a,"is odd")
is_even(4)
is_even(7)

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(4))
print(fact(6))

def is_sum(a,b):
    return (a+b)
print(is_sum(4,4))

def is_sum(a,b,c):
    return (a+b+c)
print(is_sum(4,4,2))

def is_sum(a,b):
    print(a+b)
is_sum(4,4)

def func(*a):
    print(a)
func(2,3,4,5)
func('hi','hello')

def func(**a):
    print(a)
func(a=1,b=2,c=3)

def func(a,b,c):
    print(a,b,c)
func(*(1,2,3))

def func(a,b,c):
    print(a,b,c)
func(*{'H':1,'e':2,'n':3})

def func(*a,**b):
    print(a)
    print(b)
func(1,2,3,H=2,e=3)

'''

