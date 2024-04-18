# 暴力解法
class Solution:
    def findLatestTime(self, s: str) -> str:
        for h in range(11, -1, -1): # 11 - 0
            for m in range(59, -1, -1): # 59 - 0
                t = f"{h:02d}:{m:02d}"
                if all(x == '?' or x == y for x, y in zip(s, t)):
                    return t
# 最重要的是要知道f-string操作
# all()
                
# if-else
class Solution:
    def findLatestTime(self, s: str) -> str:
        s = list(s)
        if s[0] == '?':
            if s[1] == '?':  
                s[0] = '1'
                s[1] = '1'
            elif int(s[1]) < 2:
                s[0] = '1'
            else:
                s[0] = '0'   
       
        if s[1] == '?':
            if s[0] == '1':
                s[1] = '1'
            else:
                s[1] = '9'
                
        if s[3] == '?':
            s[3] = '5'
        
        if s[4] == '?':
            s[4] = '9'
            
        return ''.join(s)