class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for i in strs:
            ans=tuple(sorted(i)) 
            if ans not in h:
                h[ans]=[]
            h[ans].append(i)
        return list(h.values())