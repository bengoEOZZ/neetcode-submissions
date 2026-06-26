class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupList = {}
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for s in strs:
            stringCount = [0]*26
            for c in s:
                stringCount[alpha.index(c)] += 1
            #print(stringCount)
            stringCount = tuple(stringCount)
            if stringCount not in groupList:
                groupList[stringCount] = [s]
            else:
                groupList[stringCount].append(s)
        return groupList.values()