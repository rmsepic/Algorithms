bool isMatch_naive(char * s, char * p){    
    char *t;
    char *q;
    
    for (t = s, q = p; *t != '\0' && *q != '\0'; t++, q++) {
        if (*t == *q || *q == '?') {
            continue;
        } else if (*q == '*') {
            char *u;
            u = t;
            for (; *u != '\0'; u++) {
                if (isMatch(u, q + 1) == true) {
                    return true;
                } // if
            } // for
            
            if (*u == '\0' && *(q + 1) == '\0') {
                return true;
            }
        } else {
            return false;
        }
    }
    
    
    if (*t == '\0' && *q == '\0') {
        return true;
    } else {
        // If s is empty but q begins with a * 
        for (; *t == '\0' && *q != '\0'; q++) {
            if (*q == '*') {
                // Keep going
                continue;
            } else {
                return false;
            }
        }
        
        if (*q == '\0' && *t == '\0') {
            return true;
        } else {
            return false;
        }
    }
}