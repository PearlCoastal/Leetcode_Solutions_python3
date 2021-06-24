import collections
class Solution():

    def solve(self, root):
        q = collections.deque([(root, 0)])

        dic = {0 : root.val}

        while q:
            size = len(q)
            for _ in range(size):
                cur, pos = q.popleft()
                if pos not in dic:
                    dic[pos] = cur.val
                if cur.left:
                    q.append((cur.left, pos - 1))
                if cur.right:
                    q.append((cur.right, pos + 1))
        
        ans = sorted(dic.items(), key = lambda x: x[0])
        return [x[1] for x in ans]

