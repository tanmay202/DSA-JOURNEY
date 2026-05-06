class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        # Handle negative numbers using 32-bit two's complement
        if num < 0:
            num += 2**32

        hex_chars = "0123456789abcdef"
        ans = ""

        while num > 0:
            rem = num % 16
            ans = hex_chars[rem] + ans
            num //= 16

        return ans