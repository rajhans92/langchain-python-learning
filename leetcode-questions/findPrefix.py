class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        lengOfWord = min(len(s) for s in strs)
        preFix= ""

        for i in range(lengOfWord):
            temp=strs[0][i]
            for j in range(len(strs)):            
                if temp != strs[j][i]:
                    return preFix
            preFix = preFix+""+ strs[j][i]

        return preFix