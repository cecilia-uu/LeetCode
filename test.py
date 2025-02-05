import math
def minimumIncrements(nums, target) -> int:
        # every target in targets
        target = list(set(target))
        ans = [float("inf")] * len(target)
        print(ans)
        print(target)
        for i, t in enumerate(target):
            for n in nums:
                if n % t == 0:
                    ans[i] = 0
                    break
                else:
                    ans[i] = min(ans[i], t - (n % t))
        ans1 = sum(ans)
        print("ans", ans) 
        if len(target) == 1:
            return ans1
         
        ans2 = float("inf")
        t = math.lcm(target[0], target[1])
        for x in target[2:]:
            t = math.lcm(t, x)

        for n in nums:
            if n % t == 0:
                return 0
            else:
                ans2 = min(ans2, t - (n % t))
        return min(ans1, ans2)

print(minimumIncrements(nums=[8,10,9], target=[10,6]))