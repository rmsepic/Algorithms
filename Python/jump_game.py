from typing import List
        
def jump_school(place: int, nums: List[int]):
    print("Place ", place, nums[place])
    # The digit at this place will take us to the end
    if nums[place] + place >= len(nums) - 1:
        return True

    flag = False
    for i in range(1, nums[place] + 1):
        if jump_school(place + i, nums):
            flag = True

    return flag

def canJump(nums: List[int]) -> bool:
    if nums[0] >= len(nums) - 1:
        return True
    
    flag = False
    for i in range(1, nums[0] + 1):
        if jump_school(i, nums):
            flag = True
            
    return flag

if __name__ == "__main__":
    #nums = [3,2,1,0,4]
    #nums = [1,1,1,0]
    nums = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
    print(canJump(nums))