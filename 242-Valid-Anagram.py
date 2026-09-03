class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen1 = {}
        seen2 = {}
        for x in s:
            if x in seen1:
                seen1[x] += 1
            else:
                seen1[x] = 1
        for y in t:
            if y in seen2:
                seen2[y] += 1
            else:
                seen2[y] = 1
        for i in seen1:
            if i in seen2:
                if seen1[i] != seen2[i]:
                    return False
            else:
                return False
        return True
