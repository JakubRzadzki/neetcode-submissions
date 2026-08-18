class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        result = []
        
        sorted_nums = sorted(nums)

        for i in range(0, l):
            left = i + 1
            right = l - 1

            while left < right:
                sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
               
                if sum == 0:
                    triplet = [sorted_nums[i], sorted_nums[left], sorted_nums[right]] 
                    left += 1
                    right -= 1

                    if triplet in result:
                        continue
                    else:
                        result.append(triplet)

                if sum < 0:
                    left += 1

                if sum > 0:
                    right -= 1
        
        return result
                
                
