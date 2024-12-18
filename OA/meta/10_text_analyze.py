def reverse(t):
    t = list(t)
    s, e = 1, len(t) - 2
    while s < e:
        t[s], t[e] = t[e], t[s]
        s += 1
        e -= 1
    return "".join(t)

def solution(text):
    # return [str]
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i, t in enumerate(text):
        if t[0] in vowels and t[-1] in vowels and len(t) > 3:
            new_t = reverse(t)
            text[i] = new_t
    
    return text

print(solution(["apple", "banana", "OranGe"]))