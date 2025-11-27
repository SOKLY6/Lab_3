class Solution:
    def sortColors(self, lst: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(lst)-1):
            index_min_element = i
            for j in range(i+1, len(lst)):
                if lst[j] < lst[index_min_element]:
                    index_min_element = j
            if index_min_element != i:
                lst[i], lst[index_min_element] = lst[index_min_element], lst[i]
        return lst