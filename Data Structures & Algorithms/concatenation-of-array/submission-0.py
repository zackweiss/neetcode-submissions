class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        first_list = []
        second_list = []
        for num in nums:
            first_list.append(num)
            second_list.append(num)
        return first_list + second_list
        