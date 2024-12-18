# https://www.bilibili.com/video/BV1it421W7D8/?spm_id_from=333.337.search-card.all.click&vd_source=1f079d184f9abb71c0f8c3ad219de322
# https://personal.utdallas.edu/~besp/demo/John2010/z-algorithm.htm

class Solution:
    def matchPattern(self, pattern: str, text: str):
        new_string = pattern + "$" + text
        z = self.calculate_z(new_string)
        res = []
        for i in range(len(z)):
            if z[i] == len(pattern):
                res.append(i - len(pattern) - 1)
        return res
    
    def calculate_z(self, s):
        n = len(s)
        z = [0] * n  # 初始化
        l, r = 0, 0  # z-box的范围
        for i in range(1, len(s)):  # 0位置没有意义
            # 这两行将算法从O(n^2)优化到O(n)
            if i <= r: # 落在z-box里面
                z[i] = min(z[i-l], r-i+1) # 左边对应的z[i]/到右边界的最小值。核心思想
            # 继续向后暴力匹配
            while i + z[i] < n and s[z[i]] == s[i+z[i]]:
                l, r = i, i + z[i]
                z[i] += 1
        return z

# tests
s = Solution()
pattern = "abc"
text = "xabcabzabc"
res = s.matchPattern(pattern, text)
print(res)