 # Given a set of strings of 0's and 1's
 # Get max set of substring of 0's and 1's
 # Where the total number of 0's in the subset is less than m
 # and the total number of 1's in the subset is less than n

 def findMaxForm(strs: List[str], m: int, n: int) -> int:
        count = [(s.count('0'), s.count('1')) for s in strs]
        ht = {}
        ht[0, 0] = 0
        
        for x1, y1 in count:
            for (x2, y2), set_size in list(ht.items()):
                if x2 + x1 <= m and y2 + y1 <= n:
                    key = (x2 + x1, y2 + y1)
                    
                    if key in ht:
                        ht[key] = max(set_size + 1, ht[key])
                    else:
                        ht[key] = set_size + 1
                    
        return max(ht.values())