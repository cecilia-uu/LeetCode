def numAfterInsertion(s, t):
    x, y = t[0], t[1]
    ans = cnt_x = cnt_y = 0
    for c in t:
        if c == y:
            ans += cnt_x
            cnt_y += 1
        if c == x:
            cnt_x += 1
    return ans + max(cnt_x, cnt_y)

def numDistinct(s: str, t: str) -> int:
        """
        我们可以给他匹配也可以不匹配(因为s[0...i−1]可以还存在结果])，
        dfs(i, j) = dfs(i-1, j-1) + dfs(i-1, j) if s[i] == t[j]
        dfs(i, j) = dfs(i-1, j) if s[i] != t[j]
        """
        m, n = len(s), len(t)
        if n > m: return 0
        f = [1] + [0] * n
        for i in range(1, m+1):
            pre = 1
            for j in range(1, n+1):
                tmp = f[j]
                if s[i-1] == t[j-1]:
                    f[j] = pre + f[j]
                else:
                    f[j] = f[j]
                pre = tmp
        return f[-1]

print(numAfterInsertion(s = "rabbbit", t = "rabbit") + numDistinct(s = "rabbbit", t = "rabbit"))
print(numAfterInsertion(s = "babgbag", t = "bag") + numDistinct(s = "babgbag", t = "bag"))