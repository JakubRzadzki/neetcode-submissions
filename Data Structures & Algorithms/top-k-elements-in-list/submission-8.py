class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_of_elements = dict()

        for num in nums:
            if num in frequency_of_elements:
                frequency_of_elements[num] += 1
            else:
                frequency_of_elements[num] = 1

        sorted_values = sorted(
            frequency_of_elements,
            key = frequency_of_elements.get,
            reverse=True
            )
        returning_value = list(sorted_values)

        return returning_value[:k]