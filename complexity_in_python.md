Python 中内置方法的时间复杂度大合集👊
====

## 列表 List

| Operation | Big-O Efficiency |
|:---:|:---:|
| append() | O(1) |
| pop() | O(1) |
| pop(0) | O(n) |
| insert(index, x) | O(n) |
| sort() | O(nlogn) |
| index(x) | O(1) |
| min() | O(n) |
| max() | O(n) |
| len() | O(1) |
| x in array| O(n) |
| remove(x)| O(n) |


## 双向队列 collections.deque()

deque 是以双向链表的形式实现的。

deque 的两端都是可达的， 但查找队列中间元素时较慢， 增删元素就更慢。

| Operation | Big-O Efficiency |
|:---:|:---:|
| append(x) | O(1) |
| appendleft(x) | O(1) |
| pop() | O(1) |
| popleft() | O(1) |
| remove | O(n) |


## 集合 set()

| Operation | Big-O Efficiency |
|:---:|:---:|
| x in s | O(1) |


## 字典 dict()

对象的散列函数足够 robust 的话， 就不会发生哈希冲突。

| Operation | Big-O Efficiency |
|:---:|:---:|
| dic[key] = value | O(1) |
| del dic[key] | O(1) |
| dic[key] | O(1) |
| dic[key] = new_value | O(1) |
| len() | O(1) |
| key in dic | O(1) |

关于 Python 的一些小问题
====

## Question 1. 列表 sort() 时间复杂度是 O(nlogn)

Python 中的 sorted() 排序内部实现是 Timsort.

讲解的话， 看这篇笔记就可以了📒 👉 [Python sort函数内部实现原理](https://www.cnblogs.com/clement-jiao/p/9243066.html)

## Question 2. python 的多线程为什么被称为伪多线程

知乎的这位答主回答的挺好， 起码我看懂了一点点。 👉 [为什么有人说 Python 的多线程是鸡肋呢？ - DarrenChan 陈驰的回答 - 知乎](https://www.zhihu.com/question/23474039/answer/269526476)

以下为个人笔记。

python 代码的执行由 python 虚拟机(解释器) 来控制。

Python 解释器可以运行多个线程， 但是只有一个线程在解释器中运行。

就像单 CPU 的系统中运行多个进程一样， 内存中虽然可以存放多个程序， 但是任意时刻， 只有一个程序在 CPU 中运行。

对 Python 虚拟机的访问由 全局解释器锁 (GIL) 来控制， 而这个锁，就能够保证只有一个线程在运行。

在多线程环境下， Python 虚拟机按照以下方式执行。

1. 设置全局解释器锁 GIL
2. 切换到一个线程去执行。
3. 执行线程。
4. 把线程设置为睡眠状态。
5. 解锁 GIL。
6. 开启新的一轮循环， 重复 1-5 。

## Question 3. Python 中 "is" "==" 的区别

Python 中对象包含的三个基本要素： 

1. id: 身份标识
2. type: 数据类型
3. value: 值

- is 比较的是 id
- == 比较的是 value

## Question 4. *args, **kwargs 的作用是什么， 如何使用

*args 和 **kwargs 通常使用在函数定义里。

两者的区别是打包参数的形式。

- *args 用来将参数打包成 tuple 给函数体调用。
- **kwargs 打包成 dic 给函数体调用。

## Question 5. lambda函数

lambda() 是匿名函数，使用 lambda函数 省略了用 def 声明函数的标准步骤。

### Python 中的赋值， 浅拷贝， 深拷贝的区别

赋值：= 相当于是创建了对象的一个新的引用， 修改其中任意一个变量都会影响到另一个。

浅拷贝： 创建一个新的对象， 但是它包含了对原始对象中包含项的引用。 如果用引用的方式修改其中一个对象， 那另一个也会相应改变。

举个🌰： 
    1. copy 模块的 copy()
    2. list()
    3. 完全切片

深拷贝：创建一个新的对象，并且递归复制他所包含的对象。 所以修改其中一个，另外一个不会改变。

举个🌰：
    1. copy 模块的 deep.deepcopy()

## Question 6. 多线程 和 多进程

进程在执行过程中拥有独立的内存单元， 进程下的多个线程可并发执行、共享同一个进程的内存， 从而提高了程序的运行效率。

线程不能独立执行， 必须依存在进程中。

线程的执行开销小， 但不利于资源的保护和管理。

进程的执行开销大， 但是有利于资源的保护和管理。

## Question 7. 随机生成一个数
```python

import random
print(random.random()) # 0-1 的数
print(random.randint(1, 100)) # 1-100 以内的整数

```
## Question 8. 函数式编程

函数式编程的定义： 允许将函数作为参数进行传递，还允许返回一个函数。

Python 对函数式编程提供部分支持， 但是由于 Python 允许使用变量，所以 Python 不是纯函数式编程语言。

