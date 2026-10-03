class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a={}
        for s in strs:
            b=''.join(sorted(s))
            if b not in a:
                a[b]=[]
            a[b].append(s)
        return list(a.values())
        