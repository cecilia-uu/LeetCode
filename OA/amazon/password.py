"""
the old password is a subsequence of the new password
similar: change the characters in the subsequece
"""
def solution(newPasswords, oldPasswords):
    def transform(s):
        if s != 'z':
            s = chr(ord(s) + 1)
        else:
            s = 'a'
        return s

    def is_similar(newPassword, oldPassword):
        len_new = len(newPassword)
        len_old = len(oldPassword)
        if len_old > len_new:
            return "NO"
        i, j = 0, 0
        while i < len_new and j < len_old:
            if oldPassword[j] == newPassword[i] or oldPassword[j] == transform(newPassword[i]):
                j += 1
            i += 1
        return "YES" if j == len_old else "NO"
        
    ans = []
    for old, new in zip(oldPasswords, newPasswords):
        ans.append(is_similar(new, old))
    return ans

# example1:
newPasswords = ["baacbab", "accbd", "baacba"]
oldPasswords = ["abdbc", "ach", "abb"]
print(solution(newPasswords, oldPasswords))
