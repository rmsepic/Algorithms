

// Left word is the word left in the order

bool compareRest(char *left, char *right, char *order, int order_idx) {
    printf("Left: %s    Right: %s\n", left, right);
    
    // If the left and right words were the same
    if (left[0] == '\0' && right[0] == '\0') {
        return true;
    } else if (left[0] == '\0') {
        return true;
    } else if (right[0] == '\0') {
        return false;
    }
    
    if (left[0] == right[0]) {
        return compareRest(++left, ++right, order, order_idx);
    } else {
        // They don't match so make sure they are in order         
        while (left[0] != order[order_idx] && right[0] != order[order_idx]) {
            order_idx++;
            // Overflowed the order
            if (order_idx >= 26) {
                return false;
            }
        }
        
        if (right[0] == order[order_idx]) {
            return false;
        }
    }

    return true;
}

bool isAlienSorted(char ** words, int wordsSize, char * order){
    // Only one word so it has to be sorted
    if (wordsSize == 1) {
        return true;
    }
    
    int order_idx = 0;
    int word_idx = 0;
    
    for (; word_idx + 1 < wordsSize; word_idx++) {
        // If they match
        if (words[word_idx][0] == words[word_idx + 1][0]) {
            if (compareRest(words[word_idx], words[word_idx + 1], order, order_idx) == false){
                return false;
            }            
        } else {
            while (words[word_idx][0] != order[order_idx] && words[word_idx + 1][0] != order[order_idx]) {
                order_idx++;
                // Overflowed the order
                if (order_idx >= 26) {
                    return false;
                }                    
            }
            
            if (words[word_idx + 1][0] == order[order_idx]) {
                return false;
            }
        }
    }
    
    return true;
}