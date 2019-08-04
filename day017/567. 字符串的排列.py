class Solution:
    # 时间复杂度O(S+T)，空间复杂度O(S+T)
    def getCharDict(self, s: str) -> dict:
        charDict1 = {}
        for c in s:
            if c in charDict1:
                charDict1[c] = charDict1[c]+1
            else:
                charDict1[c] = 1
        return charDict1

    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        charDict1 = self.getCharDict(s1)
        tempCharDict = self.getCharDict(s2[0:l1])
        for index2 in range(l2-l1+1):
            if index2 != 0:
                lastC = s2[index2-1]
                newC = s2[index2+l1-1]
                tempCharDict[lastC] = tempCharDict[lastC]-1
                if tempCharDict[lastC] == 0:
                    del tempCharDict[lastC]
                if newC in tempCharDict:
                    tempCharDict[newC] = tempCharDict[newC]+1
                else:
                    tempCharDict[newC] = 1
            if tempCharDict.__eq__(charDict1):
                return True
        return False
