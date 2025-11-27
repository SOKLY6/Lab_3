class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = Counter(nums)
        result = []
        lst = [[] for _ in range(len(nums) + 1)]
        for num, count in dictt.items():
            lst[count].append(num)
        for i in range(len(lst)-1, 0, -1):
            for num in lst[i]:
                result.append(num)
                if len(result) == k:
                    return result