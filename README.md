# Leetcode solution note

Leetcode的题目按照 **数据结构/算法** 分类的题目集合仓库， 大部分的题目有 md 解释代码， 从菜鸟角度解释算法。

> [剑指Offer](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/README.md#%E5%89%91%E6%8C%87offer)<br>
>[动态规划](https://github.com/PearlCoastal/Leetcode_GitOn#%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92)<br>
>[前缀和+滑动窗口 大合集](https://github.com/PearlCoastal/Leetcode_GitOn#%E5%89%8D%E7%BC%80%E5%92%8C%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3-%E5%A4%A7%E5%90%88%E9%9B%86)<br>
>[贪心算法](https://github.com/PearlCoastal/Leetcode_GitOn#%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95)<br>
>[二分法](https://github.com/PearlCoastal/Leetcode_GitOn#%E4%BA%8C%E5%88%86%E6%B3%95)<br>
>[滑动窗口](https://github.com/PearlCoastal/Leetcode_GitOn#%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3)<br>
>[DFS/BFS+回溯+剪枝](https://github.com/PearlCoastal/Leetcode_GitOn#dfsbfs-%E5%9B%9E%E6%BA%AF-%E5%89%AA%E6%9E%9D)<br>
>[哈希表](https://github.com/PearlCoastal/Leetcode_GitOn#%E5%93%88%E5%B8%8C%E8%A1%A8)<br>
>[单链表](https://github.com/PearlCoastal/Leetcode_GitOn#%E5%8D%95%E9%93%BE%E8%A1%A8)<br>
>[数组](https://github.com/PearlCoastal/Leetcode_GitOn#%E6%95%B0%E7%BB%84)<br>
>[二叉树](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/README.md#%E4%BA%8C%E5%8F%89%E6%A0%91)<br>
>[双指针](https://github.com/PearlCoastal/Leetcode_GitOn#%E5%8F%8C%E6%8C%87%E9%92%88)<br>
>[字符串](https://github.com/PearlCoastal/Leetcode_GitOn#%E5%AD%97%E7%AC%A6%E4%B8%B2)<br>
>[Trie](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/README.md#trie)<br>
>[堆](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/README.md#%E5%A0%86)<br>
>[并查集](https://github.com/PearlCoastal/Leetcode_GitOn#%E5%B9%B6%E6%9F%A5%E9%9B%86)<br>
>[设计数据结构](https://github.com/PearlCoastal/Leetcode_GitOn#%E8%AE%BE%E8%AE%A1%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84)<br>    


📒动态规划📒
====

1.  [[300] Longest_Increasing_Subsequence](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/DynamicProcessing/300.%E6%9C%80%E9%95%BF%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97.md)
2.  [[1143] 最长公共子序列](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/DynamicProcessing/1143.%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97.md)
3.  [打家劫舍 I II III 合集](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/DynamicProcessing/198.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8D.md)
4.  [[746] 使用最小花费爬楼梯](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/DynamicProcessing/746.%E4%BD%BF%E7%94%A8%E6%9C%80%E5%B0%8F%E8%8A%B1%E8%B4%B9%E7%88%AC%E6%A5%BC%E6%A2%AF.md)
5.  [[435] 无重叠区间](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/DynamicProcessing/435.%E6%97%A0%E9%87%8D%E5%8F%A0%E5%8C%BA%E9%97%B4.md)
6.  [[452] 用最少数量的箭引爆气球](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/DynamicProcessing/452.%E7%94%A8%E6%9C%80%E5%B0%91%E6%95%B0%E9%87%8F%E7%9A%84%E7%AE%AD%E5%BC%95%E7%88%86%E6%B0%94%E7%90%83.md)
7.  [[673] 最长递增子序列的个数](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/DynamicProcessing/673.%E6%9C%80%E9%95%BF%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97%E7%9A%84%E4%B8%AA%E6%95%B0.md)
8.  [[62] 不同路径](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/DynamicProcessing/62.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84.md)
9.  [[63] 不同路径 II](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/DynamicProcessing/63.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84-ii.md)
10.  [[64] 最小路径和](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/DynamicProcessing/64.%E6%9C%80%E5%B0%8F%E8%B7%AF%E5%BE%84%E5%92%8C.md)
11.  [[688] “马”在棋盘上的概率](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/DynamicProcessing/688.%E9%A9%AC-%E5%9C%A8%E6%A3%8B%E7%9B%98%E4%B8%8A%E7%9A%84%E6%A6%82%E7%8E%87.md)
12.  [[416] 分割等和子集](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/DynamicProcessing/416.%E5%88%86%E5%89%B2%E7%AD%89%E5%92%8C%E5%AD%90%E9%9B%86.md)
13.  [[322] 零钱兑换](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/DynamicProcessing/322.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2.md)
14.  [[96] 不同的二叉搜索树](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/96_%E4%B8%8D%E5%90%8C%E7%9A%84%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.md) 
15.  [[139] 单词拆分](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/DynamicProcessing/139.md)  
16.  [[124] 二叉树的最大路径和](https://github.com/PearlCoastal/Leetcode_GitOn/tree/master/DynamicProcessing#:~:text=12%20days%20ago-,124.md,-Create%20124.md)

📒前缀和+滑动窗口 大合集📒
====
1. [sliding window is sliding](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/prefix_slidingWindow.md)

📒贪心算法📒
====
1.  [[455] 分发饼干](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Greedy/455.%E5%88%86%E5%8F%91%E9%A5%BC%E5%B9%B2.md)
2.  [[881] 救生艇](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Greedy/881.%E6%95%91%E7%94%9F%E8%89%87.md)
3.  [[1846] 减小和重新排列数组后的最大元素](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Greedy/1846.md)
4.  [[1877] 数组中最大数对和的最小值](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Greedy/1877.md)

📒二分法📒
====
[📒二分法的笔记📒](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/BinarySearch/Note_BinarySearch.md)
1.  [[374] 猜数字大小](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/BinarySearch/374.%E7%8C%9C%E6%95%B0%E5%AD%97%E5%A4%A7%E5%B0%8F.py)
2.  [[81] 搜索旋转排序数组 II](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/BinarySearch/BinarySearch_81.%E6%90%9C%E7%B4%A2%E6%97%8B%E8%BD%AC%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84-ii.py)
3.  [[875] 爱吃香蕉的珂珂](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/BinarySearch/BinarySearch_875.%E7%88%B1%E5%90%83%E9%A6%99%E8%95%89%E7%9A%84%E7%8F%82%E7%8F%82.py)
4.  [[33] 搜索旋转排序数组](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/BinarySearch/BinarySearch_BinarySearch_33.%E6%90%9C%E7%B4%A2%E6%97%8B%E8%BD%AC%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84.py)
5.  [[35] 搜索插入位置](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/BinarySearch/Day27_35.%E6%90%9C%E7%B4%A2%E6%8F%92%E5%85%A5%E4%BD%8D%E7%BD%AE.md)
6.  [[239] 滑动窗口最大值](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/BinarySearch/Day28_239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.py)
7.  [[69] x 的平方根](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/BinarySearch/Day29_69.x-%E7%9A%84%E5%B9%B3%E6%96%B9%E6%A0%B9.md)
8.  [[278] 第一个错误的版本](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/BinarySearch/Day30_278.%E7%AC%AC%E4%B8%80%E4%B8%AA%E9%94%99%E8%AF%AF%E7%9A%84%E7%89%88%E6%9C%AC.md)
9.  [[769] Minimum-Light-radius](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/BinarySearch/Day32_769.Minimum-Light-radius.md)
10. [[778] 水位上升的泳池中游泳](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/BinarySearch/Day34_778.%E6%B0%B4%E4%BD%8D%E4%B8%8A%E5%8D%87%E7%9A%84%E6%B3%B3%E6%B1%A0%E4%B8%AD%E6%B8%B8%E6%B3%B3.md)
11. [计数二分_第k小的距离对](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/BinarySearch/%E8%AE%A1%E6%95%B0%E4%BA%8C%E5%88%86_%E7%AC%ACk%E5%B0%8F%E7%9A%84%E8%B7%9D%E7%A6%BB%E5%AF%B9.py)
12. [能力检测二分_最小灯半径](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/BinarySearch/%E8%83%BD%E5%8A%9B%E6%B5%8B%E8%AF%95%E4%BA%8C%E5%88%86_%E6%9C%80%E5%B0%8F%E7%81%AF%E5%8D%8A%E5%BE%84.py)

📒滑动窗口📒
====
[📒滑动窗口📒](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/SlidingWindow/Note_sliding_window.md)

1.  [[1423] 可获得的最大点数](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/SlidingWindow/1423.%E5%8F%AF%E8%8E%B7%E5%BE%97%E7%9A%84%E6%9C%80%E5%A4%A7%E7%82%B9%E6%95%B0.md)
2.  [[1456] 定长子串中元音的最大数目](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/SlidingWindow/Day35_1456.%E5%AE%9A%E9%95%BF%E5%AD%90%E4%B8%B2%E4%B8%AD%E5%85%83%E9%9F%B3%E7%9A%84%E6%9C%80%E5%A4%A7%E6%95%B0%E7%9B%AE.md)
3.  [[837] 新-21-点](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/SlidingWindow/Day36_837.%E6%96%B0-21-%E7%82%B9.md)
4.  [[438] 找到字符串中所有字母异位词](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/SlidingWindow/Day37_438.%E6%89%BE%E5%88%B0%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E6%89%80%E6%9C%89%E5%AD%97%E6%AF%8D%E5%BC%82%E4%BD%8D%E8%AF%8D.md)
5.  [[76] 最小覆盖子串](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/SlidingWindow/Day38_76.%E6%9C%80%E5%B0%8F%E8%A6%86%E7%9B%96%E5%AD%90%E4%B8%B2.py)
6.  [Number of Operations to Decrement Target to Zero](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/SlidingWindow/Day39_Number%20of%20Operations%20to%20Decrement%20Target%20to%20Zero.md)

📒DFS/BFS 回溯 剪枝📒
====

1.  [[1162] 地图分析](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/how_DFS%26BFS_work_in_island/1162.%E5%9C%B0%E5%9B%BE%E5%88%86%E6%9E%90.md)
2.  [[200] 岛屿数量](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/how_DFS%26BFS_work_in_island/200.%E5%B2%9B%E5%B1%BF%E6%95%B0%E9%87%8F.py)
3.  [[695] 岛屿的最大面积](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/how_DFS%26BFS_work_in_island/695.%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%9C%80%E5%A4%A7%E9%9D%A2%E7%A7%AF.md)
4.  [[959] 由斜杠划分区域](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/how_DFS%26BFS_work_in_island/not_959.%E7%94%B1%E6%96%9C%E6%9D%A0%E5%88%92%E5%88%86%E5%8C%BA%E5%9F%9F.py)
5.  [[46][47] 全排列 I II](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Backtrack/46%2B47.md)  
6.  [[39][40] 组合总和 I II](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Backtrack/39%2B40.md)
7.  [[78][90] 子集 I II](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Backtrack/78%2B90.md)
8.  [[814] 二叉树剪枝](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Binary%20Tree/814.md)<br>

📒哈希表📒
====

1.  [[260] 只出现一次的数字 III](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/260.%20%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E6%95%B0%E5%AD%97%20III.md)
2.  [[347] 前 K 个高频元素](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/HashTable/Day20_347_TopKFrequent.md)
3.  [[560] subarraySumK](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/HashTable/560_subarraySumK.py)
4.  [[974] subArray_sum_divisible_by_K](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/HashTable/Day24_974.%E5%92%8C%E5%8F%AF%E8%A2%AB-k-%E6%95%B4%E9%99%A4%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.md)
5.  [[01] sumOf2nums](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/HashTable/Day19_01_sumOf2nums.md)
6.  [[1037] boomerang](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/HashTable/Day21_1037_boomerang.md)
7.  [[03] lengthOfLongestSubstring](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/HashTable/Day22_lengthofLongestSubstring.md)
8.  [[30] findSubstring](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/HashTable/Day23_30_findSubstring.md)
9.  [[1590] minSubarray](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/HashTable/Day25_1590_minSubarray.py)

📒单链表📒
====

1.  [[138] 复制带随机指针的链表](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/LinkedList/138.md)
2.  [[LCOF.52] 两个链表的第一个公共节点](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/LinkedList/lcof52.md)
3.  [[19] 删除链表的倒数第N个节点](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/LinkedList/19_RemoveNthNode.md)
4.  [[141] linkedListCycle](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/LinkedList/141_linkedListCycle.py)
5.  [[142] linkedListCycleII](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/LinkedList/142_linkedListCycleII.py)
6.  [[143] reorderList](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/LinkedList/143_reorderList.py)
7.  [[148] sortList](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/LinkedList/148_sortList.py)
8.  [[203] removeElement](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/LinkedList/203_removeElement.py)
9.  [[206] reverseList_doublePtr](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/LinkedList/206_reverseList_doublePtr.py)
10.  [[21] mergesortedList](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/LinkedList/21_%20mergesortedList.py)
11.  [[234] palindrome_slowFast](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/LinkedList/234_palindrome_slowFast.py)
12.  [[234] palindrome_stack](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/LinkedList/234_palindrome_stack.py)
13.  [[23] reverseKgroup](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/LinkedList/23_reverseKgroup.py)
14.  [[328] Odd Even Linked List](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/LinkedList/328_Odd%20Even%20Linked%20List.py)
15.  [[86] partition](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/LinkedList/86_partition.py)

📒数组📒
====
1.  [[01] sumof2nums](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/Array/01_sumof2nums.py)
2.  [[02] add2nums](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/Array/02_add2nums.py)
3.  [[04] Media_Of_Two_Sorted_Arrays](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/Array/04_Media_Of_Two_Sorted_Arrays.py)
4.  [[15] threeSum](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/Array/15_threeSum.py)
5.  [[20] 有效的括号](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/Array/20.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.py)
6.  [[238] productofArrayExceptItself](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/Array/238_productofArrayExceptItself.py)
7.  [[41] first_missing_positive](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/Array/41_first_missing_positive.py)

📒二叉树📒
====
1. [[104] 二叉树的最大深度](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Binary%20Tree/104.md)
2. [[513] 找树左下角的值](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Binary%20Tree/513.md)

📒双指针📒
====

1.  [[1423] 可获得的最大点数](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/2Pointers/1423.%E5%8F%AF%E8%8E%B7%E5%BE%97%E7%9A%84%E6%9C%80%E5%A4%A7%E7%82%B9%E6%95%B0.py)
2.  [[876] 链表的中间结点](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/2Pointers/Day25_876.%E9%93%BE%E8%A1%A8%E7%9A%84%E4%B8%AD%E9%97%B4%E7%BB%93%E7%82%B9.md)
3.  [[26] 删除有序数组中的重复项](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/2Pointers/Day26_26.%E5%88%A0%E9%99%A4%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E9%87%8D%E5%A4%8D%E9%A1%B9.md)
4.  [[35] 搜索插入位置](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/2Pointers/Day27_35.%E6%90%9C%E7%B4%A2%E6%8F%92%E5%85%A5%E4%BD%8D%E7%BD%AE.py)
5.  [[239] 滑动窗口最大值](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/2Pointers/Day28_239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.py)
6.  [[69] x 的平方根](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/2Pointers/Day29_69.x-%E7%9A%84%E5%B9%B3%E6%96%B9%E6%A0%B9.py)
7.  [[278] 第一个错误的版本](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/2Pointers/Day30_278.%E7%AC%AC%E4%B8%80%E4%B8%AA%E9%94%99%E8%AF%AF%E7%9A%84%E7%89%88%E6%9C%AC.py)
8.  [[1893] 检查是否区域内所有整数都被覆盖](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/2Pointers/1893.md)


📒字符串📒
====
1.  [[989] 数组形式的整数加法](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/Array/989.%E6%95%B0%E7%BB%84%E5%BD%A2%E5%BC%8F%E7%9A%84%E6%95%B4%E6%95%B0%E5%8A%A0%E6%B3%95.md)
2.  [[344] reverse_string](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/String/344_reverse_string.py)
3.  [[415] add_strings](https://github.com/PearlCoastal/VSCode_GitOn/blob/master/String/415_add_strings.py)
4.  [[1736] 替换隐藏数字得到的最晚时间](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/String/1736.md)

📒设计数据结构📒
====
1. [[232] 用栈实现队列](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/232%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.md)
2. [[225] 用队列实现栈](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/225.%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0%E6%A0%88.md)
3. [面试题 03.01. 三合一](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/0301%E4%B8%89%E5%90%88%E4%B8%80.md)
4. [[155] 最小栈](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/LC155.md) 
5. [[146] LRU 缓存机制](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/LinkedList/146.md)   


📒Trie📒
====
1. [[208] 实现 Trie](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Trie/208_CreateTrie.md)
2. [[677] 键值映射](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Trie/677.md)

📒堆📒
====
1. [[347] Top K](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Heap/TopK.md)
2. [[LCCI 17.14] 最小k个数](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Heap/LCCI1714.md)
3. [[215] 数组中的第K个最大元素](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Heap/215.md)

📒并查集📒
====
1. [建立并查集](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Union-find%20Algorithm/create_UF.py)
2. [[547] 省份数量](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Union-find%20Algorithm/547.md)
3. [[924] 减少恶意软件的传播](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Union-find%20Algorithm/924.%E5%B0%BD%E9%87%8F%E5%87%8F%E5%B0%91%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6%E7%9A%84%E4%BC%A0%E6%92%AD.md)
4. [[1319] 连通网络的操作次数](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/Union-find%20Algorithm/1319.%E8%BF%9E%E9%80%9A%E7%BD%91%E7%BB%9C%E7%9A%84%E6%93%8D%E4%BD%9C%E6%AC%A1%E6%95%B0.md)

📒剑指offer📒
====
1. [剑指 Offer 11. 旋转数组的最小数字](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/%E5%89%91%E6%8C%87offer/lcof11.md)
2. [剑指 Offer 12. 矩阵中的路径](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/%E5%89%91%E6%8C%87offer/lcof12.md)
3. [剑指 Offer 52. 两个链表的第一个公共节点](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/%E5%89%91%E6%8C%87offer/lcof52.md)
4. [剑指 Offer 42. 连续子数组的最大和](https://github.com/PearlCoastal/Leetcode_GitOn/blob/master/%E5%89%91%E6%8C%87offer/42.md)
5. []()
6. []()
