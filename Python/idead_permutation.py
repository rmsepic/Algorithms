def isIdealPermutation(A: List[int]) -> bool:
        if (len(A) <= 2):
            return True
        
        for i in range(0, len(A)):
            if A[i] - i > 1 or A[i] - i < -1:
                return False
                        
        return True