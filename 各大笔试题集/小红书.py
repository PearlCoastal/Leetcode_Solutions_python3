
#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

class Solution:
    def newmate(self, text):
        # Write Code Here 
        ans = 0
        line = list(map(int, text.strip().split(' ')))
        line = line[1: ]
        line.sort()
        ans = line[len(line) - 1]
        for i in range(len(line) - 2, -1, -1):
            if ans + line[i] >= ans:
                ans += line[i]
            else:
                break
        return ans

try:
    _text = input()
except:
    _text = None

  
s = Solution()
res = s.newmate(_text)
print(res)