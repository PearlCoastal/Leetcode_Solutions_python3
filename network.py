def solution(A:list, B:list, n:int):
    # graph  = [set() for _ in range(n+1)]
    roads = zip(A,B)

    dic = {}
    for i in roads:
        if i[0] in dic: dic[i[0]] += 1
        else: dic[i[0]] = 1
        if i[1] in dic: dic[i[1]] += 1
        else: dic[i[1]] = 1
    rank = sorted(dic.items(), key=lambda item:item[1], reverse = True)
    l = len(rank)
    if l == 0: return 0
    if rank[0][1] == rank[1][1]: flag = rank[0][1] #找出第一大和第二大出度。前两个不相等，说明值分别为一二的出度
    else: flag = rank[1][1] #相等则意味着是第一大和第二大出度相等
    temp = 0
    l = len(rank)
    for i in range(l):
        if rank[i][1] < flag: #找到遍历的范围
            temp = i - 1
            break
    if temp == 0: temp == l - 1
    if flag == rank[0][1]: # 第一大和第二大出度相等
        for i in range(temp):
            for j in range(i + 1, temp + 1):
                if [rank[i][0], rank[j][0]] not in roads and [rank[j][0], rank[i][0]] not in roads:
                    return rank[0][1] * 2
        return rank[0][1] * 2 - 1
    else:  # 第一大和第二大出不相等
        for i in range(1, temp + 1):
            if [rank[i][0], rank[0][0]] not in roads and [rank[0][0], rank[i][0]] not in roads:
                return rank[0][1] + rank[i][1]
        return rank[0][1] + rank[i][1] - 1






result = solution(A=[1,2,3,3], B=[2,3,1,4], n = 4)
result