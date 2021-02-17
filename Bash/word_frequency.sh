# Leetcode Problem

# Count the number of times a word appears in a certain file

cat words.txt | tr -s ' ' '\n' | grep -v ^$ | sort | uniq -c | sort -nr | awk '{print $2, $1}'

