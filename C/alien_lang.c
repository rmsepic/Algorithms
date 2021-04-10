//bool compareRest 

bool isAlienSorted(char ** words, int wordsSize, char * order){
    // Only one word so it has to be sorted
    if (wordsSize == 1) {
        return true;
    }
    
    int order_idx = 0;
    int word_idx = 0;
    
    for (; word_idx + 1 < wordsSize; word_idx++) {
        printf("%s %s\n", words[word_idx], words[word_idx + 1]);
        // If they match
        if (strcmp(words[word_idx], words[word_idx + 1]) == 0) {
           // if (compareRest(word, next, ord) == false){
           //     return false;
           // }            
        } else {
            // They don't match so make sure they are in order
            if (words[word_idx][0] == order[order_idx]) {
                // In the correct order
                // Update the order 
                while (words[word_idx + 1][0] != order[order_idx]) {
                    order_idx++;
                    // Overflowed the order
                    if (order_idx >= 26) {
                        return false;
                    }
                    
                    //printf("ord %c %c\n", words[word_idx][0], order[order_idx]);
                }
            }
        }
    }
    
    return true;
}