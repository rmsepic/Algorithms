def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    for i in s:
        for x, j in enumerate(t):
            if i == j:
                t = t.replace(j, "",1)
                break
            print(t)
        
    if len(t) == 0:
        return True

    return False

