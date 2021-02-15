from typing import List

def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
	ans = []
	#while len(ans) != k:
	x = len(mat) // 2

	for i in range(0, len(mat)):
		# Civilian
		if mat[i][x] == 0:
			ans.append(i)

		
	
	print(ans)	

