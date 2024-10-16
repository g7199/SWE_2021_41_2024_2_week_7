from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dic = {}
    for idx, num in enumerate(nums):
        c = target - num

        if c in dic:
            return [dic[c], idx]

        dic[num] = idx
