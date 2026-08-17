class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        get_key = count.most_common(k)
        result = []
        for elm, frequency in get_key:
            result.append(elm)

        return result