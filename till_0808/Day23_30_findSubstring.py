from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:

        if not s or not words:
            return []
        
        str_len = len(s)
        words_len = len(words[0])
        words_str_len = len(words)

        dic_words = defaultdict(int)
        for words in words:
            dic_words[words] += 1

        ans = []

        for i in range(0, str_len - words_len * words_str_len + 1):

            cur_str = s[i: i + words_len * words_str_len]
            #哈希表拷贝
            temp_dic = dic_words.copy()

            for j in range(i, i + words_len * words_str_len, words_len):
                #一个子串一个字串扫描
                parts = s[j: j + words_len]

                if parts in temp_dic and temp_dic[parts] != 0:
                    temp_dic[parts] -= 1
                    #引入bool变量帮助判断
                    match = True  
                else:
                    match = False
                    break
          
            if match:
                ans.append(i)
        
        return ans


# s = "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]

ob = Solution()
ans = ob.findSubstring(s, words)
ans