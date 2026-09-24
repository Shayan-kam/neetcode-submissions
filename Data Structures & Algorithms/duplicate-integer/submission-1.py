# use a hashmap to go therouhg each value then store each value then move on to next value checking your stred values and the if a match  is found return true

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False



        