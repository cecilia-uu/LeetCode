# 第k大/小的问题有一定程度上会和二分相关。
# 可以再看看第1201题
# TODO: 第k大/小的问题集合（二分法解）。
# TODO: 二进制
"""
1. 交并集
|A|B| = |A| + |B| - |A&B|
|A|B|C| = |A| + |B| + |C| - |A&B| - |A&C| - |C&B|
-> 规律：1）动态规划的一个展开，2）里面的元素是奇数，前面就是正号；反之，就是负号
"""
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # 枚举子集
        # 二进制枚举
        n = len(coins)
        def check(m: int) -> bool:
            """
            这个函数的作用是检查给定的金额 m 是否满足条件：
            即由这组硬币能够组成的金额中，有多少个小于等于 m。
            如果满足条件，返回 True，否则返回 False。
            """
            cnt = 0  # counter
            for i in range(1, 1 << n): # 对硬币的所有子集进行枚举。这里使用了位运算的技巧，1 << n 表示 2 的 n 次方，即表示了所有可能的子集的个数。
                lcm_res = 1 # 用于存储当前子集中硬币的最小公倍数
                for j, x in enumerate(coins):
                    if i >> j & 1: # 检查当前子集中是否包含第 j 个硬币, 这里类似是模拟是交集还是并集
                        lcm_res = lcm(lcm_res, x) # 如果当前子集包含第 j 个硬币，则更新最小公倍数 lcm_res
                # 集合i对cnt的贡献
                c = m // lcm_res # 计算当前子集对于金额 m 的贡献，即当前子集中硬币的组合数量。
                cnt += c if i.bit_count() % 2 else -c # 根据当前子集的大小（奇偶性）来更新计数器 cnt。如果子集中硬币的数量是奇数个，就加上 c，否则减去 c。
            return cnt >= k # 返回是否满足条件，即找到的金额数量是否大于等于 k。
        
        left = k - 1 # 一定不满足要求
        right = min(coins) * k # 一定可以满足要求
        while left + 1 < right: # 开始二分查找，当左边界和右边界相差 1 时结束。
            mid = (left + right) // 2
            if check(mid):
                right = mid # 如果中间值满足条件，即 check(mid) 返回 True，则更新右边界为中间值。
            else:
                left = mid # 更新左边界为中间值。
        return right