# Leetcode Problem

cat transpose_file.txt | awk '{for(i=1;i<=NF;i++) s[i] = s[i] $i FS;} END {for(j=1;j<=NF;j++) print s[j];}' | sed s'/.$//'