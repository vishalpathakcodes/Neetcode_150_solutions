class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        ans = []
        for str in strs:
            freq = [0] * 26
            for char in str:
                freq[ord(char) - ord('a')] += 1
            mp[tuple(freq)].append(str)
        for freqs in mp:
            ans.append(mp[freqs])
        return ans