import sys
input_=sys.stdin

for line in input_:

    a,b=map(int,line.split(' '))

    print(a+b)

'''

import sys
input_=sys.stdin
for i, j in enumerate(input_):
    if i !=0:
        a,b=map(int,j.split(" "))
        print(a+b)


import sys
while True:
    arr = sys.stdin.readline()
    a,b = map(int, arr.split())
    if a==0 and b==0:
        break
    result = a+b
    print(result)

第一行是输入数组数量
l = list(map(int, input().split()))
while len(l) != 1 or l[0] != 0:
    print(sum(l[1:]))
    l = list(map(int, input().split()))

第一行没有输入数组数量
只要输入就一直算下去
import sys
x = sys.stdin
for i in x:
        l= list(map(int,i.split()))
        a = l[0]
        if a== 0:break
        print(sum(l[1:]))


strip()去除头尾空格
import sys
sz = int(input().strip())
print(' '.join(sorted(input().strip().split())))

or
import sys
n = int(input())
N = list(input().split(" "))
print(" ".join(sorted(N)))


什么时候用stdin
什么时候用input()
import sys
x = sys.stdin
for i in x:

    print(' '.join(sorted(i.split())))

import sys
while True:
    try:
        i = list(input().split(","))
        print(",".join(sorted(i)))
    except:
        break

'''


'''
lailailai

lailailao
'''