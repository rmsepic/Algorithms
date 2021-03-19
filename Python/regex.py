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

    for i, norm in enumerate(s):
        # Given 'x*y'
        # prev is x
        # right is y
        if i + 1 < len(s) and s[i + 1] == '*':
            if norm == '.':
                prev = '.'
                
                if i + 2 < len(s):
                    right = [i + 2]
            else:
                prev = norm
                
                if i + 2 < len(s):
                    right = [i + 2]

        # For non special cases
        if norm == p[j]:
            j += 1
        elif norm == '.':
            j += 1
        # right is equal to j
        # Get out of the '*' special case and read the string as normal
        elif right == p[j]:
            j += 1
            prev = None
            right = None
        # x is equal to the next in j
        elif prev == p[j]:
            j += 1
        else:
            return False

    if j == len(p):
        return True
    else:
        return False


                    
        
# "aasdfasdfasdfasdfas"
# "aasdf.*asdf.*asdf.*asdf.*s"

# "a*b*"
# "aaaaaaa"

if __name__ == "__main__":
    a = ["a*b*", "a*b*", "a*", "c*a*b", "a"]
    b = ["aaaaaaa", "aaaaaaa", "aa", "aab", "aa"]
    valid = [True, True, True, True, False]

    for i in range(0, len(a)):
        print(valid[i], "\t", isMatch(b[i], a[i]))

    