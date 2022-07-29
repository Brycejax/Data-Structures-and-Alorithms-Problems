import collections

class Solution:
    def groupAnagrams(self, strs):
        hashmap = collections.defaultdict(list)

        for i in strs:
            hashmap[str(sorted(i))].append(i)
            
        return hashmap.values()