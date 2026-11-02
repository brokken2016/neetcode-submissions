class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = {}
        t_hash = {}
        i = 0
        while i < len(s):
            if s_hash.get(s[i]):
                s_hash[s[i]] += 1
            else:
                s_hash[s[i]] = 1

            if t_hash.get(t[i]):
                t_hash[t[i]] += 1
            else:
                t_hash[t[i]] = 1

            i += 1

        return s_hash == t_hash