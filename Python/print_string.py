import math

from typing import List

def print_string():
    s = "abcdefgh"
    r = 3

    l = [[] for i in range(r)]

    for i in range(0, len(s)):
        l[i % r].append(s[i])

    flat = [item for sublist in l for item in sublist]
    string = ''.join([str(elem) for elem in flat])
    print(string)

def texting(inp: int, dic: dict) -> List[str]:
    print(inp)

    if inp == 0:
        return

    order = math.floor(math.log(inp, 10))
    num = inp // (10 ** order)

    chars = dic[num] 

    for c in chars:
        texting(inp - num * (10 ** order), dic)


if __name__ == "__main__":
    dic = {1: 'abc', 2:'def', 3: 'ghi', 4:'jkl', 5: 'mno', 6: 'pqr', 7:'stu', 8: 'vww', 9: 'xyz'}

    inp = 4123

    texting(inp, dic)