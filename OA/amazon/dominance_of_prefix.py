from collections import defaultdict

def findDominance(s):
    m = len(s[0])  # Length of each string (assuming all strings have the same length)
    result = []
    
    # For each prefix length from 1 to m
    for length in range(1, m + 1):
        prefix_count = defaultdict(int)
        
        # Count occurrences of each prefix of the current length
        for string in s:
            prefix = string[:length]
            prefix_count[prefix] += 1
        
        # Find the maximum dominance for this prefix length
        max_dominance = max(prefix_count.values())
        result.append(max_dominance)
    
    return result

# example:
s = ["abc", "aaa", "aba"]
print(findDominance(s))
