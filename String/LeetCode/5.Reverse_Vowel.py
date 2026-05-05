class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        st = list(s)
        v = set("AEIOUaeiou")  

        while l < r:
            if st[l] not in v:
                l += 1
            elif st[r] not in v:
                r -= 1
            else:
                st[l], st[r] = st[r], st[l]
                l += 1
                r -= 1

        return "".join(st)