# Leetcode problem
#!/bin/bash

# Print the 10th line in a file
# 3 solutions to the same problem

sed -n 10p line_file.txt 
awk 'NR==10' line_file.tx
tail -n +10 file.txt | head -1

