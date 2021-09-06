'''
A+B 1
输入
1 5
10 20
输出
6
30
'''
import sys
for line in sys.stdin:
    a, b = line.split(' ')
    
    print(int(a) + int(b))

'''
A+B 2
输入

2
1 5
10 20
输出

6
30
'''
import sys
input = sys.stdin
for i, line in enumerate(input):
    if i!= 0:
        a, b = map(int, line.split(' '))
        print(a + b)

'''
输入

1 5
10 20
0 0
输出

6
30
'''
1. 
import sys
input = sys.stdin

for index, line in enumerate(input):
    a, b = map(int, line.split(' '))
    if a == 0 and b == 0:
        break
    print(a + b)

2. 
while True:
    line = list(map(int, input().split(' ')))
    if line[0] == 0 and line[1] == 0:
        break
    print(sum(line))
    

'''
4
输入

4 1 2 3 4
5 1 2 3 4 5
0
输出

10
15
'''
import sys

while True:
    line = list(map(int, input().split(' ')))
    num = line[0]
    if num == 0:
        break
    else:
        print(sum(line[1:]))

'''
5
输入

2
4 1 2 3 4
5 1 2 3 4 5
输出

10
15
'''

while True:
    try:
        line = list(map(int, input().split(' ')))
        if len(line) == 1:
            continue
        print(sum(line[1:]))
    except:
        break

'''
6
第一行没有输入数组数量
只要输入就一直算下去
'''
while True:
    try:
        line = list(map(int, input().split(' ')))
        print(sum(line[1:]))
    except:
        break


'''
1. 字符串
输入

5
c d a bb e
输出

a bb c d e
'''
while True:
    try:
        num = int(input())
        for _ in range(num):
            line = list(map(str, input().split(' ')))
            line.sort()
            print(" ".join(line))
    except:
        break

'''
2.

输入

a c bb
f dddd
nowcoder
输出

a bb c
dddd f
nowcoder

'''

while True:
    try:
        line = list(map(str, input().split(' ')))
        line.sort()
        print(' '.join(line))
    except:
        break

'''
3.
输入

a,c,bb
f,dddd
nowcoder
输出

a,bb,c
dddd,f
nowcoder
'''

while True:
    try:
        line = list(map(str, input().split(',')))
        line.sort()
        print(','.join(line))
    except:
        break


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