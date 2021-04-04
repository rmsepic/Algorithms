def dfs(left: int, right: int, s: str, l: List[str]):
    if (left == 0 and right == 0):
        l.append(s)
        
    if (left > 0):
        self.dfs(left - 1, right, s + '(', l)
    
    if (right > 0 and left < right):
        self.dfs(left, right - 1, s + ')', l)
        

def generateParenthesis(n: int) -> List[str]:
    l = []
    dfs(n - 1, n, '(', l)
    return l
        