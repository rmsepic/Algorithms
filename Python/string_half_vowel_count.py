class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        front = s[:half]
        back = s[half:]
        front_vowels = back_vowels = 0
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        for i in range(0, len(front)):
            if front[i] in vowels:
                front_vowels += 1
                
        for j in range(0, len(back)):
            if back[j] in vowels:
                back_vowels += 1
                
        if front_vowels == back_vowels:
            return True
        
        return False