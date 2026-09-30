class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        ans = 0
        while l <= r:
            weight = people[l] + people[r]
            if weight <= limit:
                ans += 1
                r -= 1
                l += 1
            else:
                ans += 1
                r -= 1
        return ans