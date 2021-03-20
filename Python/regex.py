# Iterate through s and match it to substrings in p
# Check for matches

# 3 special cases
    # 1. '.'
        # This is just a free character, move on
    # 2. 'x*y'
        # Only x's can appear after until 'y' is encountered
    # 3. '.*y'
        # Any character can show up until y

def isMatch(p: str, s: str) -> bool:
    j = 0
    prev = None
    right = None
    i = 0
    while i < len(s) and j < len(p):
        print("Pointers ", s[i], p[j], prev, right)
        norm = s[i]
        # Given 'x*y'
        # prev is x
        # right is y
        if i + 1 < len(s) and s[i + 1] == '*':
            if norm == '.':
                prev = '.'
                
                if i + 2 < len(s):
                    right = s[i + 2]
            else:
                prev = norm
                
                if i + 2 < len(s):
                    right = s[i + 2]

        # For non special cases
        if norm == p[j]:
            j += 1
            i += 1
        elif norm == '.' and prev == None:
            j += 1
            i += 1
        # x is equal to the next in j
        elif prev == p[j] or prev == '.':
            j += 1
        # right is equal to j
        # Get out of the '*' special case and read the string as normal
        elif right == p[j] or right == '.':
            j += 1
            prev = None
            right = None
        else:
            i += 1

    if j == len(p):
        return True
    else:
        return False


                    
        
# "aasdfasdfasdfasdfas"
# "aasdf.*asdf.*asdf.*asdf.*s"

# "a*b*"
# "aaaaaaa"

if __name__ == "__main__":
    a = ["a*b*", "a*b*", "a*", "c*a*b", "a", ".*", "mis*is*ip*.",       "mis*is*p*."]
    b = ["aaaaaaa", "aaaaaaa", "aa", "aab", "aa", "ab", "mississippi",  "mississippi"]
    valid = [True, True, True, True, False, True, True, False]

    #i = 6
    #print(valid[i], "\t", isMatch(b[i], a[i]))
    for i in range(0, len(a)):
        print(valid[i], "\t", isMatch(b[i], a[i]))

    