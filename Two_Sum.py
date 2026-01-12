# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# 정수 배열 nums와 정수 target이 주어짐, 두 숫자들의 합이 target이 되는 인덱스들을 반환
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 너는 추정해야 함 각각의 input ( 정확히 하나의 방법의 ) 그리고 너는 동일한 두개를 사용할 수 없음
# You can return the answer in any order.
# 너는 어떤 순서로든 답변할 수 있다

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if (target==nums[i]+nums[j]):
#                     return [i,j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
